# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 42.67% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 66.10% | 59.20% | 37.59% | 80.81% | 19.19% | 62.41% |
| realism | 56.53% | 52.95% | 42.20% | 63.71% | 36.29% | 57.80% |
| romanticism | 62.72% | 59.04% | 48.47% | 69.61% | 30.39% | 51.53% |
| **Mean** | **61.78%** | **57.06%** | **42.75%** | **71.37%** | **28.63%** | **57.25%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1664 | 6931 | 1646 | 2763 |
| realism | 1832 | 5519 | 3144 | 2509 |
| romanticism | 2053 | 6103 | 2665 | 2183 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 63.77% | 59.08% | 44.39% | 73.78% | 26.22% | 55.61% |
| realism | 55.79% | 52.43% | 42.32% | 62.54% | 37.46% | 57.68% |
| romanticism | 63.43% | 58.75% | 45.33% | 72.18% | 27.82% | 54.67% |
| **Mean** | **61.00%** | **56.76%** | **44.01%** | **69.50%** | **30.50%** | **55.99%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1965 | 6328 | 2249 | 2462 |
| realism | 1837 | 5418 | 3245 | 2504 |
| romanticism | 1920 | 6329 | 2439 | 2316 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 75.04% |
| realism | 72.21% |
| romanticism | 74.24% |
| **Mean** | **73.83%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1234` |
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
| Confusion Matrix | `engine\core\output\linear\2026-07-14\20-26-42_812462\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `linear__impressionism__2026-07-14_20-30-48_722.bin` | 0.05 MB |
| realism | `linear__realism__2026-07-14_20-30-48_722.bin` | 0.05 MB |
| romanticism | `linear__romanticism__2026-07-14_20-30-48_722.bin` | 0.05 MB |

Total size: `0.14 MB`


---

