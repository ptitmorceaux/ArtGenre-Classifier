# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 42.26% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 62.36% | 58.40% | 45.99% | 70.81% | 29.19% | 54.01% |
| realism | 59.72% | 55.80% | 44.00% | 67.60% | 32.40% | 56.00% |
| romanticism | 62.45% | 55.77% | 36.59% | 74.94% | 25.06% | 63.41% |
| **Mean** | **61.51%** | **56.65%** | **42.19%** | **71.12%** | **28.88%** | **57.81%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2036 | 6073 | 2504 | 2391 |
| realism | 1910 | 5856 | 2807 | 2431 |
| romanticism | 1550 | 6571 | 2197 | 2686 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 56.91% | 52.28% | 37.79% | 66.77% | 33.23% | 62.21% |
| realism | 60.22% | 55.36% | 40.73% | 69.99% | 30.01% | 59.27% |
| romanticism | 64.84% | 56.19% | 31.37% | 81.01% | 18.99% | 68.63% |
| **Mean** | **60.66%** | **54.61%** | **36.63%** | **72.59%** | **27.41%** | **63.37%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1673 | 5727 | 2850 | 2754 |
| realism | 1768 | 6063 | 2600 | 2573 |
| romanticism | 1329 | 7103 | 1665 | 2907 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 69.66% |
| realism | 66.20% |
| romanticism | 68.93% |
| **Mean** | **68.27%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1337` |
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
| Confusion Matrix | `engine\core\output\linear\2026-07-14\20-32-07_799606\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `linear__impressionism__2026-07-14_20-37-36_314.bin` | 0.05 MB |
| realism | `linear__realism__2026-07-14_20-37-36_314.bin` | 0.05 MB |
| romanticism | `linear__romanticism__2026-07-14_20-37-36_314.bin` | 0.05 MB |

Total size: `0.14 MB`


---

