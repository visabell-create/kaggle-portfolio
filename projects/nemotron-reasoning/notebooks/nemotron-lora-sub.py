"""Nemotron-3-Nano-30B rank-32 LoRA SFT -> /kaggle/working/submission.zip.

Runs on the RTX PRO 6000 Blackwell (push with --accelerator NvidiaRtxPro6000).
Sources attached via kernel-metadata.json: base model, nvidia-utility-script
(cutlass DSL / mamba), and our nemotron-reasoning-sft dataset.

Deliberate hybrid-architecture choice: NemotronH is a Mamba+attention hybrid, so
we target the Mamba mixer projections (in_proj/x_proj/dt_proj/out_proj) AND the
attention projections AND the MLP (up/down/gate) -- broader than the demo's
partial set, and more targeted than blind all-linear.
"""
import glob
import json
import math
import os
import re
import shutil
import site
import subprocess
import sys
import zipfile

# Cutlass DSL + executable Triton ptxas for Blackwell custom kernels.
# Do NOT tar the whole utility bundle into /tmp or prepend /tmp to sys.path — that
# replaces the Kaggle CUDA PyTorch with a CPU build ("Found no NVIDIA driver").
_UTIL = next(
    iter(
        glob.glob("/kaggle/usr/lib/notebooks/*/nvidia_utility_script")
        + glob.glob("/kaggle/usr/lib/notebooks/*/nvidia-utility-script")
    ),
    None,
)
if _UTIL:
    for d in glob.glob(os.path.join(_UTIL, "**/nvidia_cutlass_dsl/python_packages"), recursive=True):
        site.addsitedir(d)
    _ptx_src = os.path.join(_UTIL, "triton/backends/nvidia/bin")
    _ptx_dst = "/tmp/triton/backends/nvidia/bin"
    os.makedirs(_ptx_dst, exist_ok=True)
    for name in ("ptxas", "ptxas-blackwell"):
        src = os.path.join(_ptx_src, name)
        if os.path.isfile(src):
            dst = os.path.join(_ptx_dst, name)
            shutil.copy2(src, dst)
            os.chmod(dst, 0o755)
            print("SETUP: copied", dst)
    os.environ["TRITON_PTXAS_PATH"] = os.path.join(_ptx_dst, "ptxas")
    os.environ["TRITON_PTXAS_BLACKWELL_PATH"] = os.path.join(_ptx_dst, "ptxas-blackwell")

import torch

print("GPU:", torch.cuda.get_device_name(0))
VRAM = torch.cuda.get_device_properties(0).total_memory / 1e9
print("VRAM_GB:", round(VRAM, 1))
if VRAM < 40:
    print("INSUFFICIENT GPU (need the RTX PRO 6000). Aborting before model load.")
    sys.exit(0)

import kagglehub
from peft import LoraConfig, TaskType, get_peft_model
from transformers import (
    AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments,
)

# ------------------------------- locate inputs ----------------------------- #
MODEL_PATH = os.path.dirname(
    sorted(glob.glob("/kaggle/input/**/models/**/config.json", recursive=True)
           + glob.glob("/kaggle/input/models/**/config.json", recursive=True))[0]
)
DATA = glob.glob("/kaggle/input/**/sft_train.jsonl", recursive=True)[0]
HOLDOUT = glob.glob("/kaggle/input/**/holdout_val.csv", recursive=True)[0]
OUT = "/kaggle/working"
print("MODEL_PATH:", MODEL_PATH)
print("DATA:", DATA)

MAX_LEN = 1024
LIMIT = 6000
EVAL_ROWS = 48
BOXED = "\nPlease put your final answer inside `\\boxed{}`. For example: `\\boxed{your answer}`"


def extract_final_answer(text):
    if text is None:
        return "NOT_FOUND"
    starts = list(re.finditer(r"\\boxed\{", text))
    matches = []
    for i, m in enumerate(starts):
        s = m.end()
        e = starts[i + 1].start() if i + 1 < len(starts) else len(text)
        seg = text[s:e]
        lb = seg.rfind("}")
        matches.append(seg[:lb] if lb != -1 else seg)
    if matches:
        ne = [m.strip() for m in matches if m.strip()]
        return ne[-1] if ne else matches[-1].strip()
    m = re.findall(r"-?\d+(?:\.\d+)?", text)
    return m[-1] if m else (text.strip().splitlines() or ["NOT_FOUND"])[-1]


def verify(stored, pred):
    stored, pred = stored.strip(), pred.strip()
    if re.fullmatch(r"[01]+", stored):
        return pred.lower() == stored.lower()
    try:
        return math.isclose(float(stored), float(pred), rel_tol=1e-2, abs_tol=1e-5)
    except Exception:
        return pred.lower() == stored.lower()


tok = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
if tok.pad_token_id is None:
    tok.pad_token = tok.eos_token

model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    device_map="auto",
    trust_remote_code=True,
    dtype=torch.bfloat16,
    low_cpu_mem_usage=True,
    use_safetensors=True,
)
model.config.use_cache = False
model.gradient_checkpointing_enable()

lora = LoraConfig(
    r=32, lora_alpha=32,
    target_modules=r".*\.(in_proj|x_proj|dt_proj|out_proj|up_proj|down_proj|gate_proj|q_proj|k_proj|v_proj|o_proj|qkv_proj)$",
    lora_dropout=0.05, bias="none", task_type=TaskType.CAUSAL_LM,
)
model = get_peft_model(model, lora)
model.print_trainable_parameters()

rows = [json.loads(l) for l in open(DATA, encoding="utf-8")][:LIMIT]
feats = []
for r in rows:
    try:
        ptext = tok.apply_chat_template(
            [{"role": "user", "content": r["prompt"] + BOXED}],
            tokenize=False, add_generation_prompt=True, enable_thinking=True,
        )
    except Exception:
        ptext = r["prompt"] + BOXED + "\n"
    comp = f"{r['cot']}\n\nThe final answer is \\boxed{{{r['answer']}}}."
    p = tok(ptext, add_special_tokens=False)["input_ids"]
    c = tok(comp, add_special_tokens=False)["input_ids"] + [tok.eos_token_id]
    ids = (p + c)[:MAX_LEN]
    lab = ([-100] * len(p) + c)[:MAX_LEN]
    if len(ids) >= 8:
        feats.append({"input_ids": ids, "labels": lab})
print(f"Training on {len(feats)} examples")


class Collator:
    def __call__(self, batch):
        ml = max(len(b["input_ids"]) for b in batch)
        ids, lab, att = [], [], []
        for b in batch:
            pad = ml - len(b["input_ids"])
            ids.append(b["input_ids"] + [tok.pad_token_id] * pad)
            lab.append(b["labels"] + [-100] * pad)
            att.append([1] * len(b["input_ids"]) + [0] * pad)
        return {"input_ids": torch.tensor(ids), "labels": torch.tensor(lab),
                "attention_mask": torch.tensor(att)}


Trainer(
    model=model,
    args=TrainingArguments(
        output_dir=OUT, per_device_train_batch_size=1, gradient_accumulation_steps=16,
        num_train_epochs=1, learning_rate=2e-4, lr_scheduler_type="cosine",
        warmup_ratio=0.03, logging_steps=20, save_strategy="no", bf16=True,
        report_to="none", gradient_checkpointing=True,
    ),
    train_dataset=feats, data_collator=Collator(),
).train()

model.save_pretrained(OUT, safe_serialization=True)
print("Adapter saved.")

# ------------------------- package submission.zip --------------------------- #
ZPATH = os.path.join(OUT, "submission.zip")
if os.path.exists(ZPATH):
    os.remove(ZPATH)
with zipfile.ZipFile(ZPATH, "w", zipfile.ZIP_DEFLATED) as z:
    for name in os.listdir(OUT):
        if name.startswith("adapter"):
            z.write(os.path.join(OUT, name), arcname=name)
names = zipfile.ZipFile(ZPATH).namelist()
print("submission.zip contains:", names)
assert any(n.endswith("adapter_config.json") for n in names), "adapter_config.json missing!"
print("submission.zip OK")

# --------------------------- quick holdout eval ----------------------------- #
try:
    import csv
    from collections import defaultdict
    csv.field_size_limit(10**7)
    hv = list(csv.DictReader(open(HOLDOUT, encoding="utf-8")))[:EVAL_ROWS]
    model.config.use_cache = True
    model.gradient_checkpointing_disable()
    model.eval()
    tot, cor = defaultdict(int), defaultdict(int)
    for r in hv:
        ptext = tok.apply_chat_template(
            [{"role": "user", "content": r["prompt"] + BOXED}],
            tokenize=False, add_generation_prompt=True, enable_thinking=True,
        )
        ins = tok(ptext, return_tensors="pt").to(model.device)
        with torch.no_grad():
            out = model.generate(**ins, max_new_tokens=384, do_sample=False)
        txt = tok.decode(out[0][ins["input_ids"].shape[1]:], skip_special_tokens=True)
        ok = verify(str(r["answer"]), str(extract_final_answer(txt)))
        tot[r["family"]] += 1
        cor[r["family"]] += int(ok)
    print("=== holdout quick eval (greedy) ===")
    gt = gc = 0
    for fam in sorted(tot):
        gt += tot[fam]; gc += cor[fam]
        print(f"{fam:<18}{tot[fam]:>4}{cor[fam] / tot[fam]:>8.3f}")
    print(f"HOLDOUT_ACC {gc}/{gt} = {gc / max(gt, 1):.3f}")
except Exception as e:
    print("Holdout eval skipped:", repr(e))

print("DONE")
