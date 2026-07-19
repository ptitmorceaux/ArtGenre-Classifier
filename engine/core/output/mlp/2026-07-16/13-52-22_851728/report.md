# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 47.44% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 66.47% | 61.31% | 45.13% | 77.49% | 22.51% | 54.87% |
| realism | 62.72% | 58.82% | 47.09% | 70.55% | 29.45% | 52.91% |
| romanticism | 65.69% | 61.69% | 50.21% | 73.16% | 26.84% | 49.79% |
| **Mean** | **64.96%** | **60.61%** | **47.48%** | **73.73%** | **26.27%** | **52.52%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1998 | 6646 | 1931 | 2429 |
| realism | 2044 | 6112 | 2551 | 2297 |
| romanticism | 2127 | 6415 | 2353 | 2109 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 63.59% | 61.59% | 55.34% | 67.84% | 32.16% | 44.66% |
| realism | 57.71% | 58.51% | 60.91% | 56.11% | 43.89% | 39.09% |
| romanticism | 60.80% | 62.16% | 66.05% | 58.27% | 41.73% | 33.95% |
| **Mean** | **60.70%** | **60.75%** | **60.77%** | **60.74%** | **39.26%** | **39.23%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2450 | 5819 | 2758 | 1977 |
| realism | 2644 | 4861 | 3802 | 1697 |
| romanticism | 2798 | 5109 | 3659 | 1438 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 87.86% |
| realism | 91.20% |
| romanticism | 92.04% |
| **Mean** | **90.37%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `42` |
| Type | `mlp` |
| Alpha | `0.0005` |
| Epochs | `150` |
| NPL | `[1024, 512, 256, 1]` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `29652` |
| Total samples Test | `13004` |
| Limit per category | `9884` |
| Train positive ratio | `0.50` |
| Normalization | `standard` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 9884 | 4427 |
| realism | 9884 | 4341 |
| romanticism | 9884 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 9884 | 4942 | 4942 | **19768** |
| **realism** | 4942 | 9884 | 4942 | **19768** |
| **romanticism** | 4942 | 4942 | 9884 | **19768** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine/core/output/mlp/2026-07-16/13-52-22_851728/confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| realism | `mlp__realism__2026-07-16_15-21-39_320.bin` | 2.50 MB |
| impressionism | `mlp__impressionism__2026-07-16_15-21-39_320.bin` | 2.50 MB |
| romanticism | `mlp__romanticism__2026-07-16_15-21-39_320.bin` | 2.50 MB |

Total size: `7.51 MB`


---

