#!/usr/bin/env python3
"""Generate CATALOG.yaml from a static notebook inventory."""

from __future__ import annotations

import yaml
from pathlib import Path

USER = "valentinorayisabell"
BASE = f"https://www.kaggle.com/code/{USER}"

CHAINS = {
    "pclf": {
        "competition": "llm-classification-finetuning",
        "project": "pclf-llm-classification",
        "notebooks": [
            ("notebookd476973901", "failed", "First PCLF attempt", "failed", None),
            ("traps", "showcase", "Early baseline TRAPS pipeline", "archive", "1.08357"),
            ("fine-tuning", "showcase", "Fine-tuning experiment v2", "archive", "1.07830"),
            ("hybrid-deberta-tf-idf-ensemble", "showcase", "Best TF-IDF+DeBERTa hybrid", "showcase", "1.07741"),
            ("deberta-championship-pclf-v6", "showcase", "GPU DeBERTa championship pipeline", "wip", None),
        ],
    },
    "nemotron": {
        "competition": "nvidia-nemotron-model-reasoning-challenge",
        "project": "nemotron-reasoning",
        "notebooks": [
            ("nemotron-probe", "showcase", "Architecture and rules probe", "archive", None),
            ("nemotron-lora-train", "showcase", "Rank-32 LoRA training", "archive", None),
            ("nemotron-lora-sub", "showcase", "Submission notebook", "showcase", "0.53"),
        ],
    },
    "aimo3": {
        "competition": "ai-mathematical-olympiad-progress-prize-3",
        "project": "aimo3-math-solver",
        "notebooks": [
            ("aimo-3-submission-demo", "showcase", "Gateway and format demo", "archive", None),
            ("36-40-gpt-oss-120b-tir-dynamictime-pooling", "showcase", "GPT-OSS 120B TIR iteration", "archive", None),
            ("39-50-gpt-oss-120b-tir-dynamictime-out-pooling", "showcase", "GPT-OSS 120B TIR iteration v2", "archive", None),
            ("aimo3-foundation-solver-v3", "showcase", "Multi-strategy foundation solver", "showcase", None),
        ],
    },
}

ARCHIVE = [
    "hull-lightgbm-model",
    "trapsta-gpt",
    "finetune-gpt-oss-20b",
    "hullsol",
    "trap11",
    "626-traplord-first-note",
]

GENERIC = [
    "notebook9030838a11", "notebook0bf2d191cf", "notebook3248a09646", "notebookedf6d71cdb",
    "notebookd151fe9769", "notebookd5e7d8f476", "notebookea788b70c1", "notebook9a70e7ef0e",
    "notebook3cf4f51fca", "notebook157cc9899d", "notebook823de3c60c", "notebook2024f319c5",
    "notebook23584000a1", "notebooka6d357fae8", "notebooke61d3aa83c", "notebookd87ae179c3",
    "notebook01a0725dc5", "notebook4236976bf4", "notebookbfcbb7fa22", "notebook571e179d84",
    "notebookdffc5566d9", "notebookc9943fd6eb", "notebook7aa342bc0e222", "notebook938b9df80f",
    "notebooke16c5f8d71", "notebook89368e8205", "notebooke0cfddc7c2", "notebookea10b674a2",
    "notebookdb66d127fb", "notebook28c1a0b9fd", "notebooke7fd3fdf55", "notebook43e07327ce",
    "notebook82377dbbbb", "notebookcae78f0fa6", "notebook010c0e6576", "notebook85690e4b89",
    "notebook108c18af7f", "notebook6648ecf449", "notebook07b86bcefc", "notebook7330eebb85",
    "notebook8506531149", "notebooke8fc3f5742", "notebookaa874867fb", "notebook867420ff49",
    "notebookc2cf15d7ac", "notebook7999a8652b", "notebooked618eae50", "notebook4c43f13e53",
    "notebook77f9373c6d", "notebook5f7b187fba", "notebooke5db1d623a", "notebookfba39dbe35",
    "notebook1748e62757", "notebookab40cfd8c7", "notebook78d7300ff5", "notebook4aab80c4e5",
    "notebook87a69e27b7", "notebook738cc86a59", "notebook64e49f67cb", "notebook1a63469852",
]


def main() -> None:
    entries: list[dict] = []
    for chain_id, chain in CHAINS.items():
        parent = None
        project = chain["project"]
        for slug, _role, summary, status, score in chain["notebooks"]:
            entries.append(
                {
                    "slug": slug,
                    "title": slug,
                    "project": project,
                    "competition": chain["competition"],
                    "chain": chain_id,
                    "parent_slug": parent,
                    "status": status,
                    "public_score": score,
                    "kaggle_url": f"{BASE}/{slug}",
                    "one_line_summary": summary,
                }
            )
            parent = slug

    for slug in ARCHIVE:
        entries.append(
            {
                "slug": slug,
                "title": slug,
                "project": "archive",
                "competition": None,
                "chain": "early-experiments",
                "parent_slug": None,
                "status": "archive",
                "public_score": None,
                "kaggle_url": f"{BASE}/{slug}",
                "one_line_summary": "Early experiment notebook",
            }
        )

    for slug in GENERIC:
        entries.append(
            {
                "slug": slug,
                "title": slug,
                "project": "archive",
                "competition": None,
                "chain": "experiments",
                "parent_slug": None,
                "status": "archive",
                "public_score": None,
                "kaggle_url": f"{BASE}/{slug}",
                "one_line_summary": "Iteration / experiment notebook",
            }
        )

    out = Path(__file__).resolve().parents[1] / "CATALOG.yaml"
    payload = {
        "user": USER,
        "total_notebooks": len(entries),
        "notebooks": entries,
    }
    out.write_text(yaml.dump(payload, sort_keys=False, allow_unicode=True), encoding="utf-8")
    print(f"Wrote {len(entries)} entries to {out}")


if __name__ == "__main__":
    main()
