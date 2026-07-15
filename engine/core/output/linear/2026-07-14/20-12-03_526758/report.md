# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 42.39% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 66.88% | 58.87% | 33.77% | 83.97% | 16.03% | 66.23% |
| realism | 55.24% | 53.22% | 47.13% | 59.31% | 40.69% | 52.87% |
| romanticism | 62.67% | 58.50% | 46.55% | 70.45% | 29.55% | 53.45% |
| **Mean** | **61.60%** | **56.86%** | **42.49%** | **71.24%** | **28.76%** | **57.51%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1495 | 7202 | 1375 | 2932 |
| realism | 2046 | 5138 | 3525 | 2295 |
| romanticism | 1972 | 6177 | 2591 | 2264 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 64.66% | 59.52% | 43.39% | 75.64% | 24.36% | 56.61% |
| realism | 54.57% | 52.52% | 46.37% | 58.67% | 41.33% | 53.63% |
| romanticism | 62.88% | 57.81% | 43.27% | 72.35% | 27.65% | 56.73% |
| **Mean** | **60.70%** | **56.62%** | **44.35%** | **68.89%** | **31.11%** | **55.65%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1921 | 6488 | 2089 | 2506 |
| realism | 2013 | 5083 | 3580 | 2328 |
| romanticism | 1833 | 6344 | 2424 | 2403 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 75.01% |
| realism | 72.01% |
| romanticism | 73.86% |
| **Mean** | **73.63%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1234` |
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
| Confusion Matrix | `engine\core\output\linear\2026-07-14\20-12-03_526758\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `linear__impressionism__2026-07-14_20-16-46_480.bin` | 0.05 MB |
| realism | `linear__realism__2026-07-14_20-16-46_480.bin` | 0.05 MB |
| romanticism | `linear__romanticism__2026-07-14_20-16-46_480.bin` | 0.05 MB |

Total size: `0.14 MB`


---

