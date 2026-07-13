# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 41.39% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 62.77% | 58.89% | 46.74% | 71.04% | 28.96% | 53.26% |
| realism | 59.28% | 55.13% | 42.64% | 67.62% | 32.38% | 57.36% |
| romanticism | 60.73% | 53.95% | 34.51% | 73.39% | 26.61% | 65.49% |
| **Mean** | **60.92%** | **55.99%** | **41.30%** | **70.68%** | **29.32%** | **58.70%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2069 | 6093 | 2484 | 2358 |
| realism | 1851 | 5858 | 2805 | 2490 |
| romanticism | 1462 | 6435 | 2333 | 2774 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 63.73% | 57.39% | 37.54% | 77.24% | 22.76% | 62.46% |
| realism | 60.31% | 54.16% | 35.64% | 72.68% | 27.32% | 64.36% |
| romanticism | 62.06% | 53.01% | 27.03% | 78.98% | 21.02% | 72.97% |
| **Mean** | **62.03%** | **54.85%** | **33.40%** | **76.30%** | **23.70%** | **66.60%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1662 | 6625 | 1952 | 2765 |
| realism | 1547 | 6296 | 2367 | 2794 |
| romanticism | 1145 | 6925 | 1843 | 3091 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 82.89% |
| realism | 75.64% |
| romanticism | 78.78% |
| **Mean** | **79.10%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `42` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `100` |
| NPL | `[12288, 16, 16, 16, 1]` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `4500` |
| Total samples Test | `13004` |
| Limit per category | `1500` |
| Train positive ratio | `0.33` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 1500 | 4427 |
| realism | 1500 | 4341 |
| romanticism | 1500 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 1500 | 1500 | 1500 | **4500** |
| **realism** | 1500 | 1500 | 1500 | **4500** |
| **romanticism** | 1500 | 1500 | 1500 | **4500** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\mlp\2026-07-11\21-34-26_983380\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-11_21-37-42_037.bin` | 0.75 MB |
| realism | `mlp__realism__2026-07-11_21-37-42_037.bin` | 0.75 MB |
| romanticism | `mlp__romanticism__2026-07-11_21-37-42_037.bin` | 0.75 MB |

Total size: `2.26 MB`


---

