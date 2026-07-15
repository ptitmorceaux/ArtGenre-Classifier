# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 44.24% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 64.91% | 60.14% | 45.18% | 75.10% | 24.90% | 54.82% |
| realism | 59.69% | 56.52% | 46.97% | 66.06% | 33.94% | 53.03% |
| romanticism | 63.88% | 57.83% | 40.46% | 75.19% | 24.81% | 59.54% |
| **Mean** | **62.83%** | **58.16%** | **44.20%** | **72.12%** | **27.88%** | **55.80%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2000 | 6441 | 2136 | 2427 |
| realism | 2039 | 5723 | 2940 | 2302 |
| romanticism | 1714 | 6593 | 2175 | 2522 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 64.35% | 58.27% | 39.21% | 77.32% | 22.68% | 60.79% |
| realism | 60.18% | 56.45% | 45.22% | 67.68% | 32.32% | 54.78% |
| romanticism | 63.75% | 57.40% | 39.19% | 75.62% | 24.38% | 60.81% |
| **Mean** | **62.76%** | **57.37%** | **41.21%** | **73.54%** | **26.46%** | **58.79%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1736 | 6632 | 1945 | 2691 |
| realism | 1963 | 5863 | 2800 | 2378 |
| romanticism | 1660 | 6630 | 2138 | 2576 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 69.34% |
| realism | 66.32% |
| romanticism | 69.03% |
| **Mean** | **68.23%** |


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
| Total samples Train (chargées) | `29998` |
| Total samples Test | `13004` |
| Limit per category | `-1` |
| Train positive ratio | `0.33` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 10007 | 4427 |
| realism | 10107 | 4341 |
| romanticism | 9884 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 10007 | 10130 | 9884 | **30021** |
| **realism** | 10331 | 10107 | 9884 | **30322** |
| **romanticism** | 9884 | 9884 | 9884 | **29652** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\linear\2026-07-14\20-34-31_374596\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `linear__impressionism__2026-07-14_20-39-11_759.bin` | 0.05 MB |
| realism | `linear__realism__2026-07-14_20-39-11_759.bin` | 0.05 MB |
| romanticism | `linear__romanticism__2026-07-14_20-39-11_759.bin` | 0.05 MB |

Total size: `0.14 MB`


---

