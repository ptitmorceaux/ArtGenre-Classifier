# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 35.17% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 59.54% | 50.90% | 23.81% | 77.99% | 22.01% | 76.19% |
| realism | 55.86% | 51.95% | 40.20% | 63.71% | 36.29% | 59.80% |
| romanticism | 54.93% | 51.56% | 41.88% | 61.23% | 38.77% | 58.12% |
| **Mean** | **56.78%** | **51.47%** | **35.30%** | **67.64%** | **32.36%** | **64.70%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1054 | 6689 | 1888 | 3373 |
| realism | 1745 | 5519 | 3144 | 2596 |
| romanticism | 1774 | 5369 | 3399 | 2462 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 62.67% | 51.39% | 16.04% | 86.74% | 13.26% | 83.96% |
| realism | 57.14% | 51.01% | 32.55% | 69.47% | 30.53% | 67.45% |
| romanticism | 57.60% | 51.03% | 32.20% | 69.87% | 30.13% | 67.80% |
| **Mean** | **59.14%** | **51.14%** | **26.93%** | **75.36%** | **24.64%** | **73.07%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 710 | 7440 | 1137 | 3717 |
| realism | 1413 | 6018 | 2645 | 2928 |
| romanticism | 1364 | 6126 | 2642 | 2872 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 100.00% |
| realism | 100.00% |
| romanticism | 97.78% |
| **Mean** | **99.26%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `5678` |
| Type | `mlp` |
| Alpha | `0.01` |
| Epochs | `100` |
| NPL | `[12288, 16, 16, 1]` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `38` |
| Total samples Test | `13004` |
| Limit per category | `{'impressionism': 12, 'realism': 22, 'romanticism': 32}` |
| Train positive ratio | `0.25` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 12 | 4427 |
| realism | 15 | 4341 |
| romanticism | 11 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 12 | 18 | 18 | **48** |
| **realism** | 12 | 15 | 32 | **59** |
| **romanticism** | 12 | 22 | 11 | **45** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\mlp\2026-07-12\13-54-29_862006\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-12_13-54-33_071.bin` | 0.75 MB |
| realism | `mlp__realism__2026-07-12_13-54-33_071.bin` | 0.75 MB |
| romanticism | `mlp__romanticism__2026-07-12_13-54-33_071.bin` | 0.75 MB |

Total size: `2.25 MB`


---

