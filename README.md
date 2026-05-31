# Kaggle Competition Portfolio

Interdisciplinary ML practitioner — formal stats/GIS education at Mt. SAC + 100+ Kaggle experiments in LLM fine-tuning, reasoning systems, and reproducible pipelines.

**Progress over perfection:** each project documents iteration chains, failures, and the ideas that actually moved scores.

## Featured projects

### [PCLF — LLM Preference Classification](projects/pclf-llm-classification/)

Log-loss **1.084 → 1.077** across nine submissions. Hybrid TF-IDF ensemble → DeBERTa GPU pipeline.

### [Nemotron — Reasoning Challenge](projects/nemotron-reasoning/)

Solver-verified synthetic CoT + rank-32 LoRA on 30B model. Public score **0.53**.

### [AIMO3 — Math Solver](projects/aimo3-math-solver/)

Multi-strategy solver: programmatic templates + LLM tool-use with confidence-weighted voting.

## What I learned from failures

- **Hidden data ≠ public data** — code competitions rerun on different scale ([postmortem](docs/postmortems/pclf-hidden-data-crash.md))
- **Output files are part of the model** — assert `submission.csv` exists before submit ([postmortem](docs/postmortems/pclf-missing-submission.md))
- **Read submission rules first** — notebook-output vs direct upload ([postmortem](docs/postmortems/nemotron-submission-flow.md))

## Skills

| Area | Tools |
|------|-------|
| ML / DL | PyTorch, Transformers, LoRA/PEFT, scikit-learn |
| NLP | DeBERTa fine-tuning, preference classification, LLM eval |
| Competitions | Kaggle code comps, submission hardening, OOF validation |
| Reasoning | Synthetic CoT, programmatic solvers, TIR |

## Repository map

```
projects/          # Per-competition evolution READMEs + submission logs
docs/postmortems/  # Failure narratives
docs/ideas/        # Reusable patterns
docs/linkedin/     # Paste-ready LinkedIn content
shared/            # Extracted utilities (submission checks, solvers)
CATALOG.yaml       # Full notebook index with Kaggle URLs
articles/          # Technical article drafts
```

## Links

- **Kaggle:** [valentinorayisabell](https://www.kaggle.com/valentinorayisabell)
- **LinkedIn:** [valentino-isabell-05b286362](https://www.linkedin.com/in/valentino-isabell-05b286362/)
- **About:** [docs/about.md](docs/about.md)

## Kaggle profile bio (paste-ready)

> Interdisciplinary student @ Mt. SAC (stats, GIS, business). Self-directed AI/ML research: 100+ notebooks, Kaggle competitions (PCLF, Nemotron, AIMO3). Portfolio: github.com/visabell-create/kaggle-portfolio
