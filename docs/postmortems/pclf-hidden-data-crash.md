# Postmortem: PCLF Hidden-Data Crash (v3/v4)

## What happened

Notebook versions 3 and 4 for `llm-classification-finetuning` completed on the public dataset but failed when Kaggle reran them for scoring:

> Your notebook hit an unhandled error while rerunning your code. Note that the hidden dataset can be larger/smaller/different than the public dataset.

Both submissions returned zero bytes. No public score.

## What I was trying

Jump to a heavier DeBERTa-based pipeline to improve log-loss quickly, assuming public validation was representative of the full rerun environment.

## Root cause (likely)

- Hidden test set differs in size and edge cases from public data
- Text length / memory pressure under larger batches
- ID and merge assumptions that held on public sample but broke at scale
- Insufficient defensive checks around data loading and inference paths

## What I changed next

1. Added submission hardening: assert `submission.csv` exists with non-zero size
2. Canonicalized IDs before merge (`canonical_id` helper)
3. Capped raw text lengths before tokenization
4. Built a **TF-IDF + LinearSVC ensemble** baseline (v5) before more GPU work — score **1.07741**
5. Started v6 championship pipeline with explicit schema validation and OOF tracking

## Lesson

Code competitions score a **rerun on hidden data**, not your local output. Treat public runs as smoke tests; harden for scale, memory, and output contracts.

## Evidence

- Failed submissions: refs 51891754 (v3), 53083465 (v4)
- Recovery notebook: [hybrid-deberta-tf-idf-ensemble](https://www.kaggle.com/code/valentinorayisabell/hybrid-deberta-tf-idf-ensemble)
