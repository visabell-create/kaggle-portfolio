# LinkedIn Project Entry — PCLF

**How to add:** Profile → Add section → Projects → Add project

---

**Project name:**
LLM Preference Classification — Kaggle PCLF

**Dates:**
Sep 2025 – Present

**Description (paste this):**

Competition: LLM Classification Fine-Tuning (3-class preference prediction, log-loss metric).

Progress: 1.084 → 1.077 log-loss across 9 submissions.

Idea evolution:
• v1 — First pipeline attempt; failed because submission.csv never wrote to /kaggle/working
• v2 (TRAPS) — Baseline approach; score 1.08357
• v3–v4 — Model upgrades; crashed on Kaggle's hidden dataset (larger/different than public)
• v5 (Hybrid TF-IDF + DeBERTa ensemble) — Classical logreg + LinearSVC floor; best score 1.07741
• v6 (DeBERTa Championship pipeline) — Full GPU pipeline: 5-fold CV, A/B swap augmentation, mean-pool head, label smoothing, submission sanity checks. Target: OOF < 0.90

Best idea: Build a fast classical ensemble before spending GPU hours — it set a reliable floor and informed what the neural model needed to beat.

Key failure: Hidden-data crashes taught me to harden data loading, cap memory, and assert output files exist before notebook completion.

Skills: Python, scikit-learn, PyTorch, Transformers, DeBERTa, cross-validation, NLP

**Link:**
https://www.kaggle.com/code/valentinorayisabell/hybrid-deberta-tf-idf-ensemble
