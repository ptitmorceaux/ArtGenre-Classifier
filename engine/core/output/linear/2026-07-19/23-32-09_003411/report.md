# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 41.22% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 60.31% | 57.02% | 46.71% | 67.33% | 32.67% | 53.29% |
| realism | 60.54% | 54.59% | 36.72% | 72.47% | 27.53% | 63.28% |
| romanticism | 61.59% | 56.03% | 40.08% | 71.98% | 28.02% | 59.92% |
| **Mean** | **60.81%** | **55.88%** | **41.17%** | **70.59%** | **29.41%** | **58.83%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2068 | 5775 | 2802 | 2359 |
| realism | 1594 | 6278 | 2385 | 2747 |
| romanticism | 1698 | 6311 | 2457 | 2538 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 59.83% | 58.69% | 55.12% | 62.26% | 37.74% | 44.88% |
| realism | 56.62% | 53.72% | 44.99% | 62.45% | 37.55% | 55.01% |
| romanticism | 55.95% | 53.43% | 46.18% | 60.68% | 39.32% | 53.82% |
| **Mean** | **57.47%** | **55.28%** | **48.76%** | **61.79%** | **38.21%** | **51.24%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2440 | 5340 | 3237 | 1987 |
| realism | 1953 | 5410 | 3253 | 2388 |
| romanticism | 1956 | 5320 | 3448 | 2280 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 56.38% |
| realism | 55.47% |
| romanticism | 56.52% |
| **Mean** | **56.12%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `42` |
| Type | `linear` |
| Alpha | `0.0001` |
| Epochs | `100` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `29652` |
| Total samples Test | `13004` |
| Limit per category | `9884` |
| Train positive ratio | `0.50` |
| Normalization | `standard` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 9884 | 4427 |
| realism | 9884 | 4341 |
| romanticism | 9884 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 9884 | 4942 | 4942 | **19768** |
| **realism** | 4942 | 9884 | 4942 | **19768** |
| **romanticism** | 4942 | 4942 | 9884 | **19768** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine/core/output/linear/2026-07-19/23-32-09_003411/confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| romanticism | `linear__romanticism__2026-07-19_23-32-19_403.bin` | 0.00 MB |
| impressionism | `linear__impressionism__2026-07-19_23-32-19_403.bin` | 0.00 MB |
| realism | `linear__realism__2026-07-19_23-32-19_403.bin` | 0.00 MB |

Total size: `0.01 MB`


---

