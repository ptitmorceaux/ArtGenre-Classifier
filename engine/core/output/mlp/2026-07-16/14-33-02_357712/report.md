# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 45.17% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 65.22% | 60.52% | 45.81% | 75.24% | 24.76% | 54.19% |
| realism | 61.29% | 56.61% | 42.52% | 70.69% | 29.31% | 57.48% |
| romanticism | 63.83% | 59.54% | 47.21% | 71.86% | 28.14% | 52.79% |
| **Mean** | **63.45%** | **58.89%** | **45.18%** | **72.60%** | **27.40%** | **54.82%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2028 | 6453 | 2124 | 2399 |
| realism | 1846 | 6124 | 2539 | 2495 |
| romanticism | 2000 | 6301 | 2467 | 2236 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 67.20% | 56.75% | 24.01% | 89.50% | 10.50% | 75.99% |
| realism | 65.61% | 52.78% | 14.17% | 91.39% | 8.61% | 85.83% |
| romanticism | 68.16% | 56.36% | 22.52% | 90.20% | 9.80% | 77.48% |
| **Mean** | **66.99%** | **55.30%** | **20.23%** | **90.36%** | **9.64%** | **79.77%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1063 | 7676 | 901 | 3364 |
| realism | 615 | 7917 | 746 | 3726 |
| romanticism | 954 | 7909 | 859 | 3282 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 81.62% |
| realism | 77.98% |
| romanticism | 78.80% |
| **Mean** | **79.47%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1337` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `50` |
| NPL | `[1024, 32, 16, 1]` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `20229` |
| Total samples Test | `13004` |
| Limit per category | `-1` |
| Train positive ratio | `0.25` |
| Normalization | `standard` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 6671 | 4427 |
| realism | 6738 | 4341 |
| romanticism | 6820 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 6671 | 10130 | 9884 | **26685** |
| **realism** | 10331 | 6738 | 9884 | **26953** |
| **romanticism** | 10331 | 10130 | 6820 | **27281** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\mlp\2026-07-16\14-33-02_357712\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-16_14-35-57_450.bin` | 0.13 MB |
| realism | `mlp__realism__2026-07-16_14-35-57_450.bin` | 0.13 MB |
| romanticism | `mlp__romanticism__2026-07-16_14-35-57_450.bin` | 0.13 MB |

Total size: `0.38 MB`


---

