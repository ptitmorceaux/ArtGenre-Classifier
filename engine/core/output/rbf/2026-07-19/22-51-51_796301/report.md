# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 45.97% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 58.17% | 65.03% | 86.54% | 43.52% | 56.48% | 13.46% |
| realism | 66.52% | 53.32% | 13.61% | 93.03% | 6.97% | 86.39% |
| romanticism | 67.26% | 59.37% | 36.73% | 82.00% | 18.00% | 63.27% |
| **Mean** | **63.98%** | **59.24%** | **45.63%** | **72.85%** | **27.15%** | **54.37%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 3831 | 3733 | 4844 | 596 |
| realism | 591 | 8059 | 604 | 3750 |
| romanticism | 1556 | 7190 | 1578 | 2680 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 35.97% | 51.39% | 99.73% | 3.05% | 96.95% | 0.27% |
| realism | 35.85% | 50.86% | 96.01% | 5.70% | 94.30% | 3.99% |
| romanticism | 34.07% | 50.80% | 98.80% | 2.79% | 97.21% | 1.20% |
| **Mean** | **35.29%** | **51.02%** | **98.18%** | **3.85%** | **96.15%** | **1.82%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 4415 | 262 | 8315 | 12 |
| realism | 4168 | 494 | 8169 | 173 |
| romanticism | 4185 | 245 | 8523 | 51 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 58.36% |
| realism | 52.14% |
| romanticism | 54.90% |
| **Mean** | **55.13%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `2024` |
| Type | `rbf` |
| Alpha | `0.0001` |
| Epochs | `150` |


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
| Confusion Matrix | `engine/core/output/rbf/2026-07-19/22-51-51_796301/confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| realism | `rbf__realism__2026-07-19_22-53-06_834.bin` | 0.06 MB |
| romanticism | `rbf__romanticism__2026-07-19_22-53-06_834.bin` | 0.06 MB |
| impressionism | `rbf__impressionism__2026-07-19_22-53-06_834.bin` | 0.06 MB |

Total size: `0.19 MB`


---

