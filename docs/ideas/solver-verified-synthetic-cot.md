# Idea: Solver-Verified Synthetic Chain-of-Thought

**Source:** Nemotron reasoning pipeline (`nemotron-probe` → `nemotron-lora-train` → `nemotron-lora-sub`)

## Pattern

Generate synthetic CoT training data only when a programmatic solver confirms the final answer.

## Why it works

- Filters hallucinated or inconsistent reasoning traces before SFT
- Targets hard puzzle families (bit manipulation, symbols) where coverage is measurable
- Beats blind config sweeping on public CoT dumps when domain solvers exist

## Ceiling discovered

Bit-manipulation puzzles with nonlinear circuits (~19% solver coverage) — identified **before** expensive LoRA training.

## When to reuse

Reasoning fine-tunes, math/code datasets, any domain where cheap verifiers exist.
