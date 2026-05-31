# Publishing to GitHub

`gh` CLI is not installed on this machine. Push manually:

```powershell
cd "C:\Users\Authorized User\kaggle-portfolio"
git init
git add .
git commit -m "Add Kaggle competition portfolio: progress docs, postmortems, catalog, LinkedIn pack"
git branch -M main
git remote add origin https://github.com/visabell-create/kaggle-portfolio.git
git push -u origin main
```

Create the empty repo first at: https://github.com/new → name `kaggle-portfolio` → Public

## Notebook pulls

Kaggle CLI `kernels pull` failed (SSL). Showcase notebook **sources live on Kaggle** — see each project's `notebooks/README.md`.

When CLI works:

```bash
kaggle kernels pull valentinorayisabell/hybrid-deberta-tf-idf-ensemble -p projects/pclf-llm-classification/notebooks/
```

## Kaggle profile bio

Paste from [README.md](README.md) Kaggle bio section, or:

> Interdisciplinary student @ Mt. SAC (stats, GIS, business). Self-directed AI/ML research: 100+ notebooks, Kaggle competitions (PCLF, Nemotron, AIMO3). Portfolio: github.com/visabell-create/kaggle-portfolio
