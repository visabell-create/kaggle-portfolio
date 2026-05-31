# LinkedIn Post 1 — Failure story

**When to post:** After updating your profile. Good for engagement.

---

My Kaggle notebook passed locally. Then it crashed on hidden data.

I was iterating on LLM preference classification (Kaggle PCLF). Versions 3 and 4 looked fine on the public dataset — then Kaggle reran them on a hidden test set that was larger and different.

Error: "Your notebook hit an unhandled error while rerunning your code."

What I was trying: jump straight to a bigger DeBERTa model to improve log-loss.

What actually happened: edge cases in text length, memory, and ID formatting that only show up at scale.

What I changed:
→ Assert submission.csv exists with non-zero bytes before notebook ends
→ Canonicalize ID formats (int/float/str mismatches break merges)
→ Cap text lengths before tokenization
→ Build a fast TF-IDF ensemble baseline first (score: 1.077) before GPU fine-tuning

The score didn't come from one breakthrough. It came from treating each failure as data about what the pipeline couldn't handle yet.

Full notebook chain: kaggle.com/valentinorayisabell

#MachineLearning #Kaggle #LLM #LearningInPublic
