# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 42.49% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 61.63% | 55.76% | 37.36% | 74.16% | 25.84% | 62.64% |
| realism | 59.81% | 55.82% | 43.81% | 67.83% | 32.17% | 56.19% |
| romanticism | 63.54% | 59.14% | 46.51% | 71.77% | 28.23% | 53.49% |
| **Mean** | **61.66%** | **56.91%** | **42.56%** | **71.25%** | **28.75%** | **57.44%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1654 | 6361 | 2216 | 2773 |
| realism | 1902 | 5876 | 2787 | 2439 |
| romanticism | 1970 | 6293 | 2475 | 2266 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 61.56% | 52.98% | 26.09% | 79.86% | 20.14% | 73.91% |
| realism | 63.27% | 55.90% | 33.75% | 78.06% | 21.94% | 66.25% |
| romanticism | 66.00% | 57.48% | 33.03% | 81.93% | 18.07% | 66.97% |
| **Mean** | **63.61%** | **55.45%** | **30.95%** | **79.95%** | **20.05%** | **69.05%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1155 | 6850 | 1727 | 3272 |
| realism | 1465 | 6762 | 1901 | 2876 |
| romanticism | 1399 | 7184 | 1584 | 2837 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 74.78% |
| realism | 72.52% |
| romanticism | 73.31% |
| **Mean** | **73.54%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `2024` |
| Type | `linear` |
| Alpha | `0.01` |
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
| Confusion Matrix | `engine\core\output\linear\2026-07-14\20-24-08_060188\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `linear__impressionism__2026-07-14_20-28-11_701.bin` | 0.05 MB |
| realism | `linear__realism__2026-07-14_20-28-11_701.bin` | 0.05 MB |
| romanticism | `linear__romanticism__2026-07-14_20-28-11_701.bin` | 0.05 MB |

Total size: `0.14 MB`


---

