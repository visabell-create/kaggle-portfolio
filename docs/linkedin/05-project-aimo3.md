# LinkedIn Project Entry — AIMO3 Math Solver

**How to add:** Profile → Add section → Projects → Add project

---

**Project name:**
AIMO3 — Multi-Strategy Mathematical Reasoning Solver

**Dates:**
Dec 2025 – Apr 2026

**Description (paste this):**

Competition: AI Mathematical Olympiad Progress Prize 3 — solve olympiad-level math problems under strict time limits, output integer answers 0–99999.

Progress: Evolved from submission demos through GPT-OSS 120B TIR experiments to a foundation solver architecture (v3).

Idea evolution:
• Submission demos — Learned competition gateway API and output format
• GPT-OSS 120B + TIR — Tool-integrated reasoning with dynamic timeout and pooling ([36/40] → [39/50] iterations)
• Foundation Solver v3 — Modular multi-strategy pipeline:
  - Pattern extraction (LaTeX parsing, boxed answers)
  - Template solvers (GCD, LCM, modular exponentiation, combinatorics, number theory)
  - LLM reasoning + TIR fallback when programmatic strategies miss
  - Confidence-weighted voting across all strategies

Best idea: Don't bet everything on one LLM call. Layer fast deterministic solvers first, use LLM+code execution only when templates fail. Log every strategy hit for debugging.

Key insight: Many olympiad problems reduce to template operations if you parse LaTeX correctly and normalize the problem text first.

Skills: Python, algorithm design, LLM inference, tool-use (TIR), mathematical reasoning, competition APIs

**Link:**
https://www.kaggle.com/code/valentinorayisabell/aimo3-foundation-solver-v3
