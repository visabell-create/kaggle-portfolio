# AIMO3 — Multi-Strategy Math Solver

**Competition:** [AI Mathematical Olympiad Progress Prize 3](https://www.kaggle.com/competitions/ai-mathematical-olympiad-progress-prize-3)  
**Type:** Code competition — gateway API, integer answers 0–99999

## Problem

Solve olympiad-level math under per-problem time limits using a Kaggle evaluation gateway.

## Timeline

| Stage | Notebook | Notes |
|-------|----------|-------|
| Demo | [aimo-3-submission-demo](https://www.kaggle.com/code/valentinorayisabell/aimo-3-submission-demo) | Gateway integration |
| LLM+TIR | [36-40-gpt-oss-120b-tir-dynamictime-pooling](https://www.kaggle.com/code/valentinorayisabell/36-40-gpt-oss-120b-tir-dynamictime-pooling) | GPT-OSS 120B iteration |
| LLM+TIR | [39-50-gpt-oss-120b-tir-dynamictime-out-pooling](https://www.kaggle.com/code/valentinorayisabell/39-50-gpt-oss-120b-tir-dynamictime-out-pooling) | Refinement |
| Foundation | [aimo3-foundation-solver-v3](https://www.kaggle.com/code/valentinorayisabell/aimo3-foundation-solver-v3) | Multi-strategy architecture |

## Best idea

**Confidence-weighted multi-strategy voting** — programmatic templates first, LLM+TIR fallback. See [idea doc](../../docs/ideas/multi-strategy-math-solver.md).

## Shared code

Number theory helpers in `shared/solvers/`.

## Run locally

Gateway requires Kaggle competition environment. Solver modules can be tested offline with sample problem dicts.
