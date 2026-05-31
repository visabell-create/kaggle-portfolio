# Postmortem: Nemotron Submission Flow Confusion

## What happened

First Nemotron submission attempts used direct CLI upload:

```bash
kaggle competitions submit -c nvidia-nemotron-model-reasoning-challenge -f submission.zip -m "..."
```

This conflicted with the competition's **notebook-output** requirement — the graded artifact must be produced by a committed Kaggle notebook run writing to `/kaggle/working/submission.zip`.

## What I was trying

Submit a locally built `submission.zip` (rank-32 LoRA adapter package) as soon as training finished, mirroring file-upload competitions.

## Root cause

Misread submission mode. Nemotron is a **code competition**: Kaggle reruns the notebook and collects output files from `/kaggle/working/`. Direct upload and notebook-output are different paths.

## What I changed next

1. Updated notebook (`nemotron-lora-sub`) to package adapter → `/kaggle/working/submission.zip`
2. Committed and ran notebook on Kaggle GPU to produce a version with output
3. Submitted with kernel reference when required: `-k valentinorayisabell/<slug> -v <version>`
4. Documented three submission modes in project README: CSV file upload, direct zip upload, notebook-output code comp

## Lesson

Read competition rules **before** burning GPU hours. Submission ops are part of the architecture.

## Evidence

- Successful submissions: refs 53229290, 53229347 — score **0.53**
- Notebook: [nemotron-lora-sub](https://www.kaggle.com/code/valentinorayisabell/nemotron-lora-sub)
