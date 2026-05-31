"""Resolve Kaggle competition input paths across dataset mount variants."""

from __future__ import annotations

import os
from typing import Iterable


def resolve_data_dir(
    required_files: Iterable[str] | None = None,
    competition_slugs: Iterable[str] | None = None,
) -> str:
    """Find a directory under /kaggle/input containing all required files."""
    need = set(required_files or {"train.csv", "test.csv", "sample_submission.csv"})
    candidates: list[str] = []
    for slug in competition_slugs or ():
        candidates.extend(
            [
                f"/kaggle/input/competitions/{slug}",
                f"/kaggle/input/{slug}",
            ]
        )
    for d in candidates:
        if os.path.isdir(d) and need.issubset(set(os.listdir(d))):
            return d
    for dirpath, _, filenames in os.walk("/kaggle/input"):
        if need.issubset(set(filenames)):
            return dirpath
    raise FileNotFoundError(
        "Competition data not found. Attach the competition dataset to this notebook."
    )
