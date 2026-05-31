# Nemotron — Model Reasoning Challenge

**Competition:** [nvidia-nemotron-model-reasoning-challenge](https://www.kaggle.com/competitions/nvidia-nemotron-model-reasoning-challenge)  
**Metric:** Accuracy (higher is better)  
**Type:** Code competition — notebook must output `submission.zip`

## Problem

Fine-tune NVIDIA Nemotron 3 Nano (30B, hybrid Mamba-attention) for reasoning; submit LoRA adapter bundle.

## Timeline

| Stage | Notebook | Score | Notes |
|-------|----------|-------|-------|
| Probe | [nemotron-probe](https://www.kaggle.com/code/valentinorayisabell/nemotron-probe) | — | Architecture + rules mapping |
| Train | [nemotron-lora-train](https://www.kaggle.com/code/valentinorayisabell/nemotron-lora-train) | — | Rank-32 LoRA SFT |
| Submit | [nemotron-lora-sub](https://www.kaggle.com/code/valentinorayisabell/nemotron-lora-sub) | **0.53** | Solver-verified CoT, 6k examples |

## Best idea

**Solver-verified synthetic CoT** — only train on examples where programmatic solvers confirm the answer. See [idea doc](../../docs/ideas/solver-verified-synthetic-cot.md).

## Failures

- Direct zip upload instead of notebook-output path ([postmortem](../../docs/postmortems/nemotron-submission-flow.md))
- Bit-family solver ~19% coverage on nonlinear circuits — scoped before more GPU spend

## Run locally

Training requires Kaggle GPU quota. Solver and data-generation logic referenced in chain notebooks on Kaggle.

## Evidence

Submission log: [submissions/scores.md](submissions/scores.md)
