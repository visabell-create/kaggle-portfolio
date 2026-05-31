# Showcase notebook export

Curated notebooks are indexed with Kaggle URLs in each project's `notebooks/README.md` and in [CATALOG.yaml](../../CATALOG.yaml).

## Attempted local pull

`kaggle kernels pull` failed on this machine (SSL error contacting api.kaggle.com). Re-run when network/auth is stable:

```bash
kaggle kernels pull valentinorayisabell/traps -p projects/pclf-llm-classification/notebooks/
kaggle kernels pull valentinorayisabell/fine-tuning -p projects/pclf-llm-classification/notebooks/
kaggle kernels pull valentinorayisabell/hybrid-deberta-tf-idf-ensemble -p projects/pclf-llm-classification/notebooks/
kaggle kernels pull valentinorayisabell/deberta-championship-pclf-v6 -p projects/pclf-llm-classification/notebooks/
kaggle kernels pull valentinorayisabell/notebookd476973901 -p projects/pclf-llm-classification/notebooks/
kaggle kernels pull valentinorayisabell/nemotron-probe -p projects/nemotron-reasoning/notebooks/
kaggle kernels pull valentinorayisabell/nemotron-lora-train -p projects/nemotron-reasoning/notebooks/
kaggle kernels pull valentinorayisabell/nemotron-lora-sub -p projects/nemotron-reasoning/notebooks/
kaggle kernels pull valentinorayisabell/aimo-3-submission-demo -p projects/aimo3-math-solver/notebooks/
kaggle kernels pull valentinorayisabell/aimo3-foundation-solver-v3 -p projects/aimo3-math-solver/notebooks/
```

## Alternative

Use Kaggle MCP `get_notebook_info` to export source JSON/scripts on demand.
