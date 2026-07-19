# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 40.10% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 61.40% | 54.39% | 32.41% | 76.37% | 23.63% | 67.59% |
| realism | 59.21% | 54.90% | 41.93% | 67.87% | 32.13% | 58.07% |
| romanticism | 59.57% | 56.13% | 46.25% | 66.01% | 33.99% | 53.75% |
| **Mean** | **60.06%** | **55.14%** | **40.20%** | **70.08%** | **29.92%** | **59.80%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1435 | 6550 | 2027 | 2992 |
| realism | 1820 | 5880 | 2783 | 2521 |
| romanticism | 1959 | 5788 | 2980 | 2277 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 61.99% | 52.48% | 22.70% | 82.27% | 17.73% | 77.30% |
| realism | 62.60% | 53.50% | 26.15% | 80.86% | 19.14% | 73.85% |
| romanticism | 62.16% | 53.71% | 29.49% | 77.94% | 22.06% | 70.51% |
| **Mean** | **62.25%** | **53.23%** | **26.11%** | **80.36%** | **19.64%** | **73.89%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1005 | 7056 | 1521 | 3422 |
| realism | 1135 | 7005 | 1658 | 3206 |
| romanticism | 1249 | 6834 | 1934 | 2987 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 65.41% |
| realism | 65.64% |
| romanticism | 66.99% |
| **Mean** | **66.01%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `42` |
| Type | `linear` |
| Alpha | `0.0001` |
| Epochs | `100` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `19767` |
| Total samples Test | `13004` |
| Limit per category | `9884` |
| Train positive ratio | `0.25` |
| Normalization | `standard` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 6589 | 4427 |
| realism | 6589 | 4341 |
| romanticism | 6589 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 6589 | 9884 | 9884 | **26357** |
| **realism** | 9884 | 6589 | 9884 | **26357** |
| **romanticism** | 9884 | 9884 | 6589 | **26357** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine/core/output/linear/2026-07-19/23-34-20_178509/confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `linear__impressionism__2026-07-19_23-34-32_462.bin` | 0.00 MB |
| realism | `linear__realism__2026-07-19_23-34-32_462.bin` | 0.00 MB |
| romanticism | `linear__romanticism__2026-07-19_23-34-32_462.bin` | 0.00 MB |

Total size: `0.01 MB`


---

