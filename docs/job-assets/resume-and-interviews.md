# Job application assets

## Resume summary (3 bullets)

- Current Mt. SAC student (Statistics, GIS, Business Admin) with 10,000+ hours self-directed AI/ML R&D and 100+ Kaggle notebooks
- Built reproducible DeBERTa fine-tuning pipeline for 3-class LLM preference prediction; improved log-loss from 1.084 → 1.077 across 9 submissions
- Designed solver-verified synthetic CoT pipeline for 30B Nemotron LoRA fine-tune (rank-32, public score 0.53); architected multi-strategy AIMO3 math solver with programmatic + LLM TIR fallback

## Project bullets (copy per role)

**PCLF / NLP / ML Engineer:**
- Iterated LLM preference classification pipeline on Kaggle (log-loss 1.084→1.077): TF-IDF ensemble baseline, DeBERTa 5-fold CV, swap augmentation, submission hardening
- Documented code-competition failure modes (hidden-data crash, missing output files) with postmortems and reusable validation utilities

**Nemotron / Research Engineer:**
- Built solver-verified synthetic chain-of-thought dataset for reasoning fine-tune; scoped programmatic solver coverage before GPU training
- Submitted rank-32 LoRA adapter to NVIDIA Nemotron Reasoning Challenge (0.53); resolved notebook-output vs direct-upload submission requirements

**AIMO3 / Applied Scientist:**
- Designed multi-strategy olympiad math solver: LaTeX parsing, template solvers, modular arithmetic, confidence-weighted voting, LLM+TIR fallback

## Interview story bank (STAR outlines)

### 1. Hidden data crash
- **S:** PCLF code competition, needed better log-loss
- **T:** Improve model without breaking Kaggle rerun
- **A:** Diagnosed v3/v4 failures; added ID canonicalization, text caps, submission asserts; built classical ensemble floor
- **R:** Stable 1.07741; clearer path to DeBERTa v6

### 2. Submission flow confusion (Nemotron)
- **S:** Had trained LoRA adapter locally
- **T:** Submit to Nemotron code competition
- **A:** Learned notebook-output requirement; updated notebook to write submission.zip to /kaggle/working
- **R:** Successful submission, score 0.53

### 3. Bit solver ceiling
- **S:** Nemotron training data from programmatic solvers
- **T:** Maximize puzzle coverage before GPU spend
- **A:** Measured bit-family coverage (~19% on nonlinear circuits); focused synthetic data on verifiable subset
- **R:** Avoided training on unverified examples; informed data strategy

### 4. Hybrid ensemble insight
- **S:** Limited GPU budget on PCLF
- **T:** Improve score efficiently
- **A:** TF-IDF + LinearSVC ensemble before DeBERTa
- **R:** 1.07741 floor; faster iteration cycle

### 5. Learning velocity
- **S:** New to Kaggle Sep 2025
- **T:** Build credible ML portfolio quickly
- **A:** 100+ notebooks, 3 competition chains, documented failures
- **R:** Portfolio repo + LinkedIn progress narrative with evidence links

## Target roles

- ML Engineer (LLM fine-tuning, evaluation)
- Applied Scientist (NLP preference / ranking)
- Research Engineer (reasoning, synthetic data)
- Data Scientist — AI/ML

## Evidence packet (one-page outline)

1. **Portfolio:** https://github.com/visabell-create/kaggle-portfolio
2. **Top notebooks:**
   - https://www.kaggle.com/code/valentinorayisabell/hybrid-deberta-tf-idf-ensemble
   - https://www.kaggle.com/code/valentinorayisabell/nemotron-lora-sub
   - https://www.kaggle.com/code/valentinorayisabell/aimo3-foundation-solver-v3
3. **Score progression:** PCLF 1.084→1.077; Nemotron 0.53
4. **Postmortem excerpt:** [pclf-hidden-data-crash.md](../postmortems/pclf-hidden-data-crash.md)
5. **LinkedIn:** https://www.linkedin.com/in/valentino-isabell-05b286362/
