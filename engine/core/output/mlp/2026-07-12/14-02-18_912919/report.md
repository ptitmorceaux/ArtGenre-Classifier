# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 35.71% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 59.50% | 51.74% | 27.40% | 76.08% | 23.92% | 72.60% |
| realism | 53.71% | 50.72% | 41.70% | 59.74% | 40.26% | 58.30% |
| romanticism | 58.21% | 53.05% | 38.27% | 67.84% | 32.16% | 61.73% |
| **Mean** | **57.14%** | **51.84%** | **35.79%** | **67.88%** | **32.12%** | **64.21%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1213 | 6525 | 2052 | 3214 |
| realism | 1810 | 5175 | 3488 | 2531 |
| romanticism | 1621 | 5948 | 2820 | 2615 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 61.04% | 51.57% | 21.91% | 81.23% | 18.77% | 78.09% |
| realism | 57.21% | 50.78% | 31.42% | 70.14% | 29.86% | 68.58% |
| romanticism | 60.95% | 51.78% | 25.45% | 78.10% | 21.90% | 74.55% |
| **Mean** | **59.73%** | **51.37%** | **26.26%** | **76.49%** | **23.51%** | **73.74%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 970 | 6967 | 1610 | 3457 |
| realism | 1364 | 6076 | 2587 | 2977 |
| romanticism | 1078 | 6848 | 1920 | 3158 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 96.61% |
| realism | 87.50% |
| romanticism | 93.41% |
| **Mean** | **92.51%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1337` |
| Type | `mlp` |
| Alpha | `0.01` |
| Epochs | `50` |
| NPL | `[12288, 16, 16, 1]` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `50` |
| Total samples Test | `13004` |
| Limit per category | `{'impressionism': 56, 'realism': 12, 'romanticism': 32}` |
| Train positive ratio | `0.25` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 15 | 4427 |
| realism | 12 | 4341 |
| romanticism | 23 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 15 | 12 | 32 | **59** |
| **realism** | 18 | 12 | 18 | **48** |
| **romanticism** | 56 | 12 | 23 | **91** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\mlp\2026-07-12\14-02-18_912919\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-12_14-02-20_767.bin` | 0.75 MB |
| realism | `mlp__realism__2026-07-12_14-02-20_767.bin` | 0.75 MB |
| romanticism | `mlp__romanticism__2026-07-12_14-02-20_767.bin` | 0.75 MB |

Total size: `2.25 MB`


---

