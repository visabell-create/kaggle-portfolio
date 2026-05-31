# Idea: DeBERTa Preference Pipeline

**Source:** [deberta-championship-pclf-v6](https://www.kaggle.com/code/valentinorayisabell/deberta-championship-pclf-v6)

## Pattern

Reproducible GPU fine-tuning for 3-class LLM preference prediction (log-loss).

## Components

| Stage | Technique |
|-------|-----------|
| Data | Schema validation, stratified 5-fold, A/B swap augmentation |
| Model | DeBERTa-v3-base + mean-pool head + dropout |
| Training | AdamW (discriminative LR), cosine warmup, label smoothing, AMP |
| Eval | Out-of-fold log-loss per fold + headline OOF metric |
| Submit | Canonical IDs, row-sum normalization, file existence asserts |

## When to reuse

Any preference/ranking task with paired text inputs and probabilistic outputs — LLM eval, RLHF data prep, A/B response selection.

## Code

See `shared/kaggle_utils/` and `projects/pclf-llm-classification/`.
