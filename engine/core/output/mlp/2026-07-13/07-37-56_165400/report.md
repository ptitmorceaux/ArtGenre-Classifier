# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 41.61% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 63.27% | 58.52% | 43.66% | 73.38% | 26.62% | 56.34% |
| realism | 59.10% | 54.75% | 41.65% | 67.85% | 32.15% | 58.35% |
| romanticism | 60.85% | 55.31% | 39.42% | 71.20% | 28.80% | 60.58% |
| **Mean** | **61.07%** | **56.20%** | **41.58%** | **70.81%** | **29.19%** | **58.42%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1933 | 6294 | 2283 | 2494 |
| realism | 1808 | 5878 | 2785 | 2533 |
| romanticism | 1670 | 6243 | 2525 | 2566 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 66.05% | 56.41% | 26.23% | 86.60% | 13.40% | 73.77% |
| realism | 62.24% | 52.89% | 24.74% | 81.03% | 18.97% | 75.26% |
| romanticism | 63.60% | 53.22% | 23.47% | 82.98% | 17.02% | 76.53% |
| **Mean** | **63.96%** | **54.18%** | **24.81%** | **83.54%** | **16.46%** | **75.19%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1161 | 7428 | 1149 | 3266 |
| realism | 1074 | 7020 | 1643 | 3267 |
| romanticism | 994 | 7276 | 1492 | 3242 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 90.59% |
| realism | 85.60% |
| romanticism | 85.60% |
| **Mean** | **87.26%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1337` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `100` |
| NPL | `[12288, 256, 256, 1]` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `2001` |
| Total samples Test | `13004` |
| Limit per category | `1000` |
| Train positive ratio | `0.25` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 667 | 4427 |
| realism | 667 | 4341 |
| romanticism | 667 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 667 | 1000 | 1000 | **2667** |
| **realism** | 1000 | 667 | 1000 | **2667** |
| **romanticism** | 1000 | 1000 | 667 | **2667** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\mlp\2026-07-13\07-37-56_165400\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-13_09-06-07_332.bin` | 12.25 MB |
| realism | `mlp__realism__2026-07-13_09-06-07_332.bin` | 12.25 MB |
| romanticism | `mlp__romanticism__2026-07-13_09-06-07_332.bin` | 12.25 MB |

Total size: `36.76 MB`


---

