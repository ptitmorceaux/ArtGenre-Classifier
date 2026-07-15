# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 38.39% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 60.06% | 55.47% | 41.11% | 69.84% | 30.16% | 58.89% |
| realism | 58.56% | 52.25% | 33.26% | 71.23% | 28.77% | 66.74% |
| romanticism | 58.16% | 53.67% | 40.79% | 66.55% | 33.45% | 59.21% |
| **Mean** | **58.93%** | **53.80%** | **38.39%** | **69.21%** | **30.79%** | **61.61%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1820 | 5990 | 2587 | 2607 |
| realism | 1444 | 6171 | 2492 | 2897 |
| romanticism | 1728 | 5835 | 2933 | 2508 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 60.84% | 56.95% | 44.75% | 69.15% | 30.85% | 55.25% |
| realism | 57.11% | 53.07% | 40.91% | 65.22% | 34.78% | 59.09% |
| romanticism | 55.54% | 51.72% | 40.75% | 62.69% | 37.31% | 59.25% |
| **Mean** | **57.83%** | **53.91%** | **42.14%** | **65.69%** | **34.31%** | **57.86%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1981 | 5931 | 2646 | 2446 |
| realism | 1776 | 5650 | 3013 | 2565 |
| romanticism | 1726 | 5497 | 3271 | 2510 |


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
| Seed | `2024` |
| Type | `linear` |
| Alpha | `0.01` |
| Epochs | `100` |


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
| Confusion Matrix | `engine\core\output\linear\2026-07-12\13-57-43_156170\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `linear__impressionism__2026-07-12_13-57-43_996.bin` | 0.05 MB |
| realism | `linear__realism__2026-07-12_13-57-43_996.bin` | 0.05 MB |
| romanticism | `linear__romanticism__2026-07-12_13-57-43_996.bin` | 0.05 MB |

Total size: `0.14 MB`


---

