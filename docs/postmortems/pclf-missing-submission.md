# Postmortem: Missing submission.csv (PCLF v1)

## What happened

First submission attempt (`notebookd476973901`, version 1) failed with:

> Your notebook did not output the expected submission file. The rerun of your notebook appears to have completed, but when we looked for your submission file, it wasn't there.

## What I was trying

Stand up an initial end-to-end pipeline for 3-class LLM preference prediction and submit quickly to learn the competition loop.

## Root cause

The notebook run finished without writing `submission.csv` to `/kaggle/working/` — either the write path was wrong, the cell order didn't reach the export step on rerun, or an early exit skipped file creation.

## What I changed next

1. Standardized output path: `/kaggle/working/submission.csv`
2. Added end-of-notebook asserts for file existence and byte size
3. Separated training vs export cells so export always runs on completion
4. Continued iteration through TRAPS → fine-tuning → hybrid ensemble chain

## Lesson

In code competitions, ** producing the contract file is part of the model**. A perfect training run that doesn't write `submission.csv` is a failed submission.

## Evidence

- Failed submission: ref 52300443
- Later successful chain starts at [traps](https://www.kaggle.com/code/valentinorayisabell/traps)
