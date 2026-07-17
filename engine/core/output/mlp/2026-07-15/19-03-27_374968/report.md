# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 44.82% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 65.33% | 60.06% | 43.53% | 76.59% | 23.41% | 56.47% |
| realism | 61.57% | 56.10% | 39.67% | 72.54% | 27.46% | 60.33% |
| romanticism | 62.75% | 59.83% | 51.46% | 68.20% | 31.80% | 48.54% |
| **Mean** | **63.22%** | **58.66%** | **44.89%** | **72.44%** | **27.56%** | **55.11%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1927 | 6569 | 2008 | 2500 |
| realism | 1722 | 6284 | 2379 | 2619 |
| romanticism | 2180 | 5980 | 2788 | 2056 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 66.26% | 56.91% | 27.60% | 86.21% | 13.79% | 72.40% |
| realism | 64.87% | 53.32% | 18.54% | 88.09% | 11.91% | 81.46% |
| romanticism | 68.33% | 56.41% | 22.19% | 90.62% | 9.38% | 77.81% |
| **Mean** | **66.49%** | **55.54%** | **22.78%** | **88.31%** | **11.69%** | **77.22%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1222 | 7394 | 1183 | 3205 |
| realism | 805 | 7631 | 1032 | 3536 |
| romanticism | 940 | 7946 | 822 | 3296 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 85.27% |
| realism | 81.20% |
| romanticism | 80.08% |
| **Mean** | **82.19%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `42` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `35` |
| NPL | `[1024, 64, 32, 1]` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `20229` |
| Total samples Test | `13004` |
| Limit per category | `-1` |
| Train positive ratio | `0.25` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 6671 | 4427 |
| realism | 6738 | 4341 |
| romanticism | 6820 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 6671 | 10129 | 9884 | **26684** |
| **realism** | 10331 | 6738 | 9884 | **26953** |
| **romanticism** | 10331 | 10129 | 6820 | **27280** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine/core/output/mlp/2026-07-15/19-03-27_374968/confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-15_19-06-20_559.bin` | 0.26 MB |
| realism | `mlp__realism__2026-07-15_19-06-20_559.bin` | 0.26 MB |
| romanticism | `mlp__romanticism__2026-07-15_19-06-20_559.bin` | 0.26 MB |

Total size: `0.78 MB`


---

