# LinkedIn Post 2 — Progress story

**When to post:** 2–3 days after Post 1.

---

How I improved log-loss from 1.084 → 1.077 without jumping to the biggest model first.

Kaggle PCLF asks you to predict which of two LLM responses a human preferred (3-class, log-loss metric).

My iteration chain:
1.084 — first working baseline (TRAPS notebook)
1.078 — fine-tuning experiment
1.077 — TF-IDF logreg + LinearSVC ensemble (hybrid-deberta-tf-idf-ensemble, v5)

The idea that moved the score: don't skip classical ML.

Before spending GPU hours on DeBERTa, I built a TF-IDF + linear model ensemble. It became the floor my neural model had to beat — and it taught me which text features actually mattered for preference prediction.

Now I'm on v6: full DeBERTa pipeline with 5-fold CV, A/B swap augmentation, mean-pool head, and submission hardening. Target: OOF log-loss < 0.90.

Progress isn't always a bigger model. Sometimes it's a cheaper one that tells you where to focus.

Notebook: kaggle.com/code/valentinorayisabell/hybrid-deberta-tf-idf-ensemble

#MachineLearning #NLP #Kaggle #DataScience
