# LinkedIn Post 3 — Innovation story

**When to post:** 2–3 days after Post 2.

---

I stopped brute-forcing LoRA configs and built solver-verified training data instead.

NVIDIA Nemotron Reasoning Challenge: fine-tune a 30B hybrid Mamba-attention model, submit the adapter as submission.zip.

Competitors were sweeping configs on public chain-of-thought datasets. I took a different path:

1. Built programmatic solvers for puzzle families (bit manipulation, symbols, modular arithmetic)
2. Ran solvers on generated puzzles — only kept examples where the solver confirmed the answer
3. Used that verified set for rank-32 LoRA SFT (6k examples)
4. Submitted via notebook output (learned that one the hard way)

The solver coverage wasn't perfect — bit-manipulation puzzles with nonlinear circuits (majority gates, choice circuits) only hit ~19%. But knowing that ceiling before GPU training saved me from training on garbage data.

Best idea I'll reuse outside competitions: if you can programmatically verify training examples, filter before you fine-tune. Data quality beats config sweeping.

Public score: 0.53 | Notebook: kaggle.com/code/valentinorayisabell/nemotron-lora-sub

#AI #LLM #FineTuning #MachineLearning #Innovation
