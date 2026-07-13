# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 41.08% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 63.01% | 59.22% | 47.32% | 71.11% | 28.89% | 52.68% |
| realism | 58.14% | 53.48% | 39.46% | 67.49% | 32.51% | 60.54% |
| romanticism | 61.01% | 54.60% | 36.21% | 72.99% | 27.01% | 63.79% |
| **Mean** | **60.72%** | **55.77%** | **41.00%** | **70.53%** | **29.47%** | **59.00%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2095 | 6099 | 2478 | 2332 |
| realism | 1713 | 5847 | 2816 | 2628 |
| romanticism | 1534 | 6400 | 2368 | 2702 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 64.36% | 54.37% | 23.04% | 85.69% | 14.31% | 76.96% |
| realism | 63.29% | 50.69% | 12.79% | 88.60% | 11.40% | 87.21% |
| romanticism | 66.13% | 52.40% | 13.01% | 91.80% | 8.20% | 86.99% |
| **Mean** | **64.60%** | **52.49%** | **16.28%** | **88.70%** | **11.30%** | **83.72%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1020 | 7350 | 1227 | 3407 |
| realism | 555 | 7675 | 988 | 3786 |
| romanticism | 551 | 8049 | 719 | 3685 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 70.94% |
| realism | 69.32% |
| romanticism | 70.24% |
| **Mean** | **70.17%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `42` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `100` |
| NPL | `[12288, 8, 8, 8, 1]` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `9000` |
| Total samples Test | `13004` |
| Limit per category | `3000` |
| Train positive ratio | `0.33` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 3000 | 4427 |
| realism | 3000 | 4341 |
| romanticism | 3000 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 3000 | 3000 | 3000 | **9000** |
| **realism** | 3000 | 3000 | 3000 | **9000** |
| **romanticism** | 3000 | 3000 | 3000 | **9000** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\mlp\2026-07-11\22-03-39_195707\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-11_22-07-33_029.bin` | 0.38 MB |
| realism | `mlp__realism__2026-07-11_22-07-33_029.bin` | 0.38 MB |
| romanticism | `mlp__romanticism__2026-07-11_22-07-33_029.bin` | 0.38 MB |

Total size: `1.13 MB`


---

