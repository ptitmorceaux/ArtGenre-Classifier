# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 34.09% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 59.47% | 52.73% | 31.58% | 73.87% | 26.13% | 68.42% |
| realism | 58.57% | 50.89% | 27.80% | 73.98% | 26.02% | 72.20% |
| romanticism | 50.14% | 48.33% | 43.15% | 53.51% | 46.49% | 56.85% |
| **Mean** | **56.06%** | **50.65%** | **34.18%** | **67.12%** | **32.88%** | **65.82%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1398 | 6336 | 2241 | 3029 |
| realism | 1207 | 6409 | 2254 | 3134 |
| romanticism | 1828 | 4692 | 4076 | 2408 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 59.62% | 54.01% | 36.41% | 71.60% | 28.40% | 63.59% |
| realism | 57.78% | 50.90% | 30.18% | 71.61% | 28.39% | 69.82% |
| romanticism | 49.91% | 47.03% | 38.76% | 55.29% | 44.71% | 61.24% |
| **Mean** | **55.77%** | **50.64%** | **35.12%** | **66.17%** | **33.83%** | **64.88%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1612 | 6141 | 2436 | 2815 |
| realism | 1310 | 6204 | 2459 | 3031 |
| romanticism | 1642 | 4848 | 3920 | 2594 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 100.00% |
| realism | 100.00% |
| romanticism | 100.00% |
| **Mean** | **100.00%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1234` |
| Type | `linear` |
| Alpha | `0.01` |
| Epochs | `50` |


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
| Confusion Matrix | `engine\core\output\linear\2026-07-12\14-01-07_244955\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `linear__impressionism__2026-07-12_14-01-07_779.bin` | 0.05 MB |
| realism | `linear__realism__2026-07-12_14-01-07_779.bin` | 0.05 MB |
| romanticism | `linear__romanticism__2026-07-12_14-01-07_779.bin` | 0.05 MB |

Total size: `0.14 MB`


---

