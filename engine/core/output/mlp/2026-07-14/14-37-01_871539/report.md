# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 41.52% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 66.54% | 58.92% | 35.06% | 82.79% | 17.21% | 64.94% |
| realism | 58.51% | 56.23% | 49.37% | 63.10% | 36.90% | 50.63% |
| romanticism | 57.98% | 53.39% | 40.23% | 66.56% | 33.44% | 59.77% |
| **Mean** | **61.01%** | **56.18%** | **41.55%** | **70.82%** | **29.18%** | **58.45%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1552 | 7101 | 1476 | 2875 |
| realism | 2143 | 5466 | 3197 | 2198 |
| romanticism | 1704 | 5836 | 2932 | 2532 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 67.14% | 58.25% | 30.38% | 86.11% | 13.89% | 69.62% |
| realism | 61.08% | 53.27% | 29.79% | 76.76% | 23.24% | 70.21% |
| romanticism | 59.27% | 52.72% | 33.90% | 71.53% | 28.47% | 66.10% |
| **Mean** | **62.50%** | **54.75%** | **31.36%** | **78.14%** | **21.86%** | **68.64%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1345 | 7386 | 1191 | 3082 |
| realism | 1293 | 6650 | 2013 | 3048 |
| romanticism | 1436 | 6272 | 2496 | 2800 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 78.00% |
| realism | 73.70% |
| romanticism | 74.97% |
| **Mean** | **75.56%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `5678` |
| Type | `mlp` |
| Alpha | `0.01` |
| Epochs | `100` |
| NPL | `[12288, 32, 1]` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `3000` |
| Total samples Test | `13004` |
| Limit per category | `1000` |
| Train positive ratio | `désactivé (-1)` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 1000 | 4427 |
| realism | 1000 | 4341 |
| romanticism | 1000 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 1000 | 1000 | 1000 | **3000** |
| **realism** | 1000 | 1000 | 1000 | **3000** |
| **romanticism** | 1000 | 1000 | 1000 | **3000** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\mlp\2026-07-14\14-37-01_871539\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-14_14-47-06_773.bin` | 1.50 MB |
| realism | `mlp__realism__2026-07-14_14-47-06_773.bin` | 1.50 MB |
| romanticism | `mlp__romanticism__2026-07-14_14-47-06_773.bin` | 1.50 MB |

Total size: `4.50 MB`


---

