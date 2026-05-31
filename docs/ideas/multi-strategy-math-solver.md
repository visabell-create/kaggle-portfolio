# Idea: Multi-Strategy Math Solver with Confidence Voting

**Source:** [aimo3-foundation-solver-v3](https://www.kaggle.com/code/valentinorayisabell/aimo3-foundation-solver-v3)

## Pattern

Layer fast deterministic solvers before LLM inference; aggregate by confidence-weighted voting.

## Strategy stack

1. Pattern extract (boxed answers, LaTeX cleanup)
2. Template compute (GCD, LCM, mod exp, combinatorics)
3. Modular arithmetic / number theory
4. LLM reasoning + TIR (tool-integrated code execution) as fallback

## When to reuse

Timed inference, olympiad-style problems, any setting where LLM-only is too slow or unreliable.

## Key insight

Log strategy hits per problem — debugging which layer failed beats tuning one monolithic prompt.
