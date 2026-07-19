# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 49.47% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 67.86% | 63.10% | 48.16% | 78.03% | 21.97% | 51.84% |
| realism | 63.14% | 59.40% | 48.12% | 70.67% | 29.33% | 51.88% |
| romanticism | 67.93% | 63.87% | 52.22% | 75.52% | 24.48% | 47.78% |
| **Mean** | **66.31%** | **62.12%** | **49.50%** | **74.74%** | **25.26%** | **50.50%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2132 | 6693 | 1884 | 2295 |
| realism | 2089 | 6122 | 2541 | 2252 |
| romanticism | 2212 | 6622 | 2146 | 2024 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 64.54% | 62.99% | 58.14% | 67.84% | 32.16% | 41.86% |
| realism | 58.21% | 59.23% | 62.31% | 56.15% | 43.85% | 37.69% |
| romanticism | 62.36% | 63.44% | 66.55% | 60.33% | 39.67% | 33.45% |
| **Mean** | **61.70%** | **61.89%** | **62.33%** | **61.44%** | **38.56%** | **37.67%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2574 | 5819 | 2758 | 1853 |
| realism | 2705 | 4864 | 3799 | 1636 |
| romanticism | 2819 | 5290 | 3478 | 1417 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 89.06% |
| realism | 86.25% |
| romanticism | 87.51% |
| **Mean** | **87.60%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `42` |
| Type | `mlp` |
| Alpha | `0.0005` |
| Epochs | `150` |
| NPL | `[1024, 1024, 512, 1]` |


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
| Confusion Matrix | `engine/core/output/mlp/2026-07-16/16-30-18_224512/confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-16_20-30-13_397.bin` | 6.01 MB |
| romanticism | `mlp__romanticism__2026-07-16_20-30-13_397.bin` | 6.01 MB |
| realism | `mlp__realism__2026-07-16_20-30-13_397.bin` | 6.01 MB |

Total size: `18.02 MB`


---

