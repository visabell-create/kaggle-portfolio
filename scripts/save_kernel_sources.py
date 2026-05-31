#!/usr/bin/env python3
"""Save Kaggle kernel source exported via MCP into project notebook folders."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Pre-exported sources keyed by slug -> (relative path, raw source string, is_notebook_json)
EXPORTS: dict[str, tuple[str, str]] = {}


def register(slug: str, relpath: str, source: str, notebook_json: bool = False) -> None:
    EXPORTS[slug] = (relpath, source, notebook_json)


def write_exports() -> None:
    for slug, (relpath, source, notebook_json) in EXPORTS.items():
        out = ROOT / relpath
        out.parent.mkdir(parents=True, exist_ok=True)
        if notebook_json:
            out.write_text(json.dumps(json.loads(source), indent=1), encoding="utf-8")
        else:
            out.write_text(source, encoding="utf-8")
        print(f"Wrote {out}")


if __name__ == "__main__":
    write_exports()
