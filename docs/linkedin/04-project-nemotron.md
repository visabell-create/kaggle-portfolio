# LinkedIn Project Entry — Nemotron Reasoning

**How to add:** Profile → Add section → Projects → Add project

---

**Project name:**
NVIDIA Nemotron Model Reasoning Challenge

**Dates:**
May 2026

**Description (paste this):**

Competition: Fine-tune NVIDIA's Nemotron 3 Nano (hybrid Mamba-attention, 30B) for reasoning tasks. Submit trained adapter as submission.zip via notebook output.

Progress: Built pipeline from probe → synthetic data generation → LoRA training → submission. Public score: 0.53.

Idea evolution:
• Probe phase — Mapped model architecture, target modules, and competition submission rules
• Solver phase — Built programmatic solvers for bit-manipulation and symbol puzzles; discovered ~19% coverage on nonlinear circuits (majority/choice gates) — identified ceiling before expensive GPU training
• Data innovation — Solver-verified synthetic CoT: only include training examples where programmatic solvers confirm the answer
• Training — Rank-32 hybrid LoRA, 6k solver-verified chain-of-thought SFT examples
• Submission ops — Learned this is a notebook-output code competition (not direct zip upload)

Best idea: Quality-filtered synthetic data beats brute-force config sweeping on public datasets. If the solver can't verify it, don't train on it.

Key failure: First submission attempt used direct file upload instead of notebook-output path (-k user/slug -v version). Reading competition rules first saves days.

Skills: LoRA/PEFT, PyTorch, synthetic data generation, LLM fine-tuning, competition ops

**Link:**
https://www.kaggle.com/code/valentinorayisabell/nemotron-lora-sub
