# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 38.71% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 60.56% | 54.44% | 35.26% | 73.62% | 26.38% | 64.74% |
| realism | 57.41% | 52.04% | 35.89% | 68.20% | 31.80% | 64.11% |
| romanticism | 59.45% | 55.77% | 45.21% | 66.33% | 33.67% | 54.79% |
| **Mean** | **59.14%** | **54.08%** | **38.79%** | **69.38%** | **30.62%** | **61.21%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1561 | 6314 | 2263 | 2866 |
| realism | 1558 | 5908 | 2755 | 2783 |
| romanticism | 1915 | 5816 | 2952 | 2321 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 60.24% | 55.99% | 42.67% | 69.30% | 30.70% | 57.33% |
| realism | 55.71% | 51.67% | 39.51% | 63.83% | 36.17% | 60.49% |
| romanticism | 56.63% | 53.93% | 46.18% | 61.68% | 38.32% | 53.82% |
| **Mean** | **57.53%** | **53.86%** | **42.78%** | **64.94%** | **35.06%** | **57.22%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1889 | 5944 | 2633 | 2538 |
| realism | 1715 | 5530 | 3133 | 2626 |
| romanticism | 1956 | 5408 | 3360 | 2280 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 97.13% |
| realism | 96.27% |
| romanticism | 94.73% |
| **Mean** | **96.04%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `5678` |
| Type | `linear` |
| Alpha | `0.001` |
| Epochs | `100` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `1500` |
| Total samples Test | `13004` |
| Limit per category | `500` |
| Train positive ratio | `0.33` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 500 | 4427 |
| realism | 500 | 4341 |
| romanticism | 500 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 500 | 500 | 500 | **1500** |
| **realism** | 500 | 500 | 500 | **1500** |
| **romanticism** | 500 | 500 | 500 | **1500** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\linear\2026-07-11\20-53-36_317761\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `linear__impressionism__2026-07-11_20-54-04_081.bin` | 0.05 MB |
| realism | `linear__realism__2026-07-11_20-54-04_081.bin` | 0.05 MB |
| romanticism | `linear__romanticism__2026-07-11_20-54-04_081.bin` | 0.05 MB |

Total size: `0.14 MB`


---

