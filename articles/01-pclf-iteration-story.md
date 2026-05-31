# From 1.084 to 1.077: Iterating on LLM Preference Classification

*Draft for Medium / dev.to / LinkedIn article*

## Hook

My Kaggle score didn't jump because I found one magic model. It moved because I treated nine submissions as an iteration lab — and built a classical baseline before touching GPU fine-tuning.

## The problem

[LLM Classification Fine-Tuning](https://www.kaggle.com/competitions/llm-classification-finetuning) asks you to predict which of two LLM responses a human preferred. Three classes, log-loss metric, code competition (notebook must output `submission.csv`).

## Timeline

| Stage | Score | Idea |
|-------|-------|------|
| TRAPS baseline | 1.08357 | First working pipeline |
| Fine-tuning | 1.07830 | Neural experiment |
| TF-IDF + LinearSVC ensemble | **1.07741** | Classical floor |
| DeBERTa v6 (WIP) | target OOF < 0.90 | Full GPU pipeline |

## What failed

**Missing submission (v1):** Notebook completed but never wrote `submission.csv`. Lesson: assert output file exists.

**Hidden-data crash (v3/v4):** Passed on public data, crashed on Kaggle rerun. Lesson: harden for scale, canonicalize IDs, cap text lengths.

Full postmortems: [pclf-missing-submission.md](../docs/postmortems/pclf-missing-submission.md), [pclf-hidden-data-crash.md](../docs/postmortems/pclf-hidden-data-crash.md)

## The idea that worked

Before DeBERTa GPU hours, I built a **TF-IDF logreg + LinearSVC ensemble**. It:

1. Set a reliable score floor (1.07741)
2. Revealed which text features mattered for preference
3. Informed what the neural model needed to beat

## DeBERTa v6 pipeline (current)

From [deberta-championship-pclf-v6](https://www.kaggle.com/code/valentinorayisabell/deberta-championship-pclf-v6):

- Stratified 5-fold CV with A/B swap augmentation
- Mean-pool head, label smoothing, mixed precision
- Shared utilities: `shared/kaggle_utils/submission.py`

```python
# Canonical ID merge — prevents silent submission gaps
sub["_kid"] = canonical_id(sub["id"]).astype(str)
pred_tbl["_kid"] = canonical_id(test_df["id"]).astype(str)
sub = sub.merge(pred_tbl, on="_kid", how="left")
```

## What I'd do differently

Start with submission hardening and classical baseline on day one. Read code-competition rerun rules before scaling model size.

## Links

- Portfolio: https://github.com/visabell-create/kaggle-portfolio
- Best notebook: https://www.kaggle.com/code/valentinorayisabell/hybrid-deberta-tf-idf-ensemble
- Project README: [projects/pclf-llm-classification/README.md](../projects/pclf-llm-classification/README.md)
