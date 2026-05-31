# PCLF — LLM Preference Classification

**Competition:** [llm-classification-finetuning](https://www.kaggle.com/competitions/llm-classification-finetuning)  
**Metric:** Log-loss (lower is better)  
**Type:** Code competition — notebook must output `submission.csv`

## Problem

Predict human preference among two LLM responses: `winner_model_a`, `winner_model_b`, or `winner_tie`.

## Timeline

| Version | Notebook | Public score | Notes |
|---------|----------|--------------|-------|
| v1 | `notebookd476973901` | — | Missing submission file ([postmortem](../../docs/postmortems/pclf-missing-submission.md)) |
| v2 | [traps](https://www.kaggle.com/code/valentinorayisabell/traps) | 1.08357 | Early baseline |
| v2 | [fine-tuning](https://www.kaggle.com/code/valentinorayisabell/fine-tuning) | 1.07830 | Fine-tuning experiment |
| v3–v4 | hybrid variants | — | Hidden-data crash ([postmortem](../../docs/postmortems/pclf-hidden-data-crash.md)) |
| v5 | [hybrid-deberta-tf-idf-ensemble](https://www.kaggle.com/code/valentinorayisabell/hybrid-deberta-tf-idf-ensemble) | **1.07741** | Best public score |
| v6 | [deberta-championship-pclf-v6](https://www.kaggle.com/code/valentinorayisabell/deberta-championship-pclf-v6) | WIP | GPU DeBERTa pipeline, target OOF < 0.90 |

## Best idea

**Hybrid classical + neural ensemble** — TF-IDF logreg + LinearSVC sets a fast, reliable floor before GPU fine-tuning. See [idea doc](../../docs/ideas/deberta-preference-pipeline.md).

## Failures

- [Missing submission.csv](../../docs/postmortems/pclf-missing-submission.md)
- [Hidden-data crash](../../docs/postmortems/pclf-hidden-data-crash.md)

## Run locally

Data stays on Kaggle. To reproduce methodology:

1. Attach competition data in a Kaggle notebook
2. Use helpers in `shared/kaggle_utils/`
3. Full pipeline in `deberta-championship-pclf-v6` on Kaggle

## Evidence

Submission log: [submissions/scores.md](submissions/scores.md)
