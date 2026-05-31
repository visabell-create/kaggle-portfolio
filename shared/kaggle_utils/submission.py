"""Submission formatting and validation helpers (from DeBERTa PCLF pipeline)."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


def canonical_id(series: pd.Series) -> pd.Series:
    """Normalize id column variants (int/float/str) for reliable merges."""

    def _one(v):
        if pd.isna(v):
            return "nan"
        try:
            fv = float(v)
            if np.isfinite(fv) and abs(fv - round(fv)) < 1e-9 * max(1.0, abs(fv)):
                return str(int(round(fv)))
        except (TypeError, ValueError):
            pass
        s = str(v).strip()
        if s.endswith(".0") and s[:-2].lstrip("-").isdigit():
            return s[:-2]
        return s

    return series.map(_one)


def validate_submission(
    sub: pd.DataFrame,
    prob_cols: list[str],
    output_path: str | Path,
) -> None:
    """Assert submission shape, probability rows, and output file existence."""
    missing = sub[prob_cols].isna().any(axis=1).sum()
    if missing:
        raise RuntimeError(f"submission has {missing} missing rows")

    row_sums = sub[prob_cols].sum(axis=1).values
    if not np.all(np.isclose(row_sums, 1.0, atol=1e-4)):
        p = sub[prob_cols].values.astype(np.float64)
        p = p / p.sum(axis=1, keepdims=True)
        sub[prob_cols] = p

    out = Path(output_path)
    sub.to_csv(out, index=False)
    if not out.is_file() or out.stat().st_size == 0:
        raise RuntimeError(f"Expected non-empty submission file: {out}")
