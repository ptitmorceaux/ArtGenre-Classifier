# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 42.14% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 62.75% | 56.08% | 35.19% | 76.97% | 23.03% | 64.81% |
| realism | 56.79% | 55.18% | 50.33% | 60.03% | 39.97% | 49.67% |
| romanticism | 64.74% | 58.61% | 41.01% | 76.21% | 23.79% | 58.99% |
| **Mean** | **61.43%** | **56.62%** | **42.18%** | **71.07%** | **28.93%** | **57.82%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1558 | 6602 | 1975 | 2869 |
| realism | 2185 | 5200 | 3463 | 2156 |
| romanticism | 1737 | 6682 | 2086 | 2499 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 65.64% | 56.20% | 26.61% | 85.79% | 14.21% | 73.39% |
| realism | 59.53% | 54.17% | 38.06% | 70.29% | 29.71% | 61.94% |
| romanticism | 65.86% | 56.14% | 28.26% | 84.02% | 15.98% | 71.74% |
| **Mean** | **63.68%** | **55.50%** | **30.97%** | **80.03%** | **19.97%** | **69.03%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1178 | 7358 | 1219 | 3249 |
| realism | 1652 | 6089 | 2574 | 2689 |
| romanticism | 1197 | 7367 | 1401 | 3039 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 74.63% |
| realism | 72.41% |
| romanticism | 73.54% |
| **Mean** | **73.52%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `2024` |
| Type | `linear` |
| Alpha | `0.001` |
| Epochs | `100` |


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
| **impressionism** | 6671 | 10130 | 9884 | **26685** |
| **realism** | 10331 | 6738 | 9884 | **26953** |
| **romanticism** | 10331 | 10130 | 6820 | **27281** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\linear\2026-07-14\20-06-08_575222\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `linear__impressionism__2026-07-14_20-10-34_153.bin` | 0.05 MB |
| realism | `linear__realism__2026-07-14_20-10-34_153.bin` | 0.05 MB |
| romanticism | `linear__romanticism__2026-07-14_20-10-34_153.bin` | 0.05 MB |

Total size: `0.14 MB`


---

