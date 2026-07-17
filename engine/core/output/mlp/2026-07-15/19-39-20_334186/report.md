# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 45.80% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 64.88% | 59.98% | 44.64% | 75.33% | 24.67% | 55.36% |
| realism | 61.39% | 57.08% | 44.11% | 70.05% | 29.95% | 55.89% |
| romanticism | 65.33% | 61.05% | 48.75% | 73.35% | 26.65% | 51.25% |
| **Mean** | **63.87%** | **59.37%** | **45.83%** | **72.91%** | **27.09%** | **54.17%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1976 | 6461 | 2116 | 2451 |
| realism | 1915 | 6068 | 2595 | 2426 |
| romanticism | 2065 | 6431 | 2337 | 2171 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 60.57% | 59.35% | 55.52% | 63.18% | 36.82% | 44.48% |
| realism | 57.50% | 57.96% | 59.36% | 56.56% | 43.44% | 40.64% |
| romanticism | 60.87% | 61.53% | 63.43% | 59.63% | 40.37% | 36.57% |
| **Mean** | **59.65%** | **59.61%** | **59.44%** | **59.79%** | **40.21%** | **40.56%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2458 | 5419 | 3158 | 1969 |
| realism | 2577 | 4900 | 3763 | 1764 |
| romanticism | 2687 | 5228 | 3540 | 1549 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 88.44% |
| realism | 90.28% |
| romanticism | 90.43% |
| **Mean** | **89.72%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `42` |
| Type | `mlp` |
| Alpha | `0.0005` |
| Epochs | `150` |
| NPL | `[1024, 256, 128, 1]` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `29652` |
| Total samples Test | `13004` |
| Limit per category | `9884` |
| Train positive ratio | `0.50` |
| Normalization | `per_column` |

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
| Confusion Matrix | `engine/core/output/mlp/2026-07-15/19-39-20_334186/confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-15_20-15-00_700.bin` | 1.13 MB |
| realism | `mlp__realism__2026-07-15_20-15-00_700.bin` | 1.13 MB |
| romanticism | `mlp__romanticism__2026-07-15_20-15-00_700.bin` | 1.13 MB |

Total size: `3.38 MB`


---

