# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 45.74% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 61.70% | 65.31% | 76.62% | 54.00% | 46.00% | 23.38% |
| realism | 64.24% | 53.88% | 22.71% | 85.05% | 14.95% | 77.29% |
| romanticism | 65.53% | 58.18% | 37.06% | 79.29% | 20.71% | 62.94% |
| **Mean** | **63.83%** | **59.12%** | **45.47%** | **72.78%** | **27.22%** | **54.53%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 3392 | 4632 | 3945 | 1035 |
| realism | 986 | 7368 | 1295 | 3355 |
| romanticism | 1570 | 6952 | 1816 | 2666 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 47.66% | 58.54% | 92.61% | 24.46% | 75.54% | 7.39% |
| realism | 41.18% | 53.32% | 89.86% | 16.78% | 83.22% | 10.14% |
| romanticism | 47.11% | 57.46% | 87.18% | 27.75% | 72.25% | 12.82% |
| **Mean** | **45.32%** | **56.44%** | **89.89%** | **23.00%** | **77.00%** | **10.11%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 4100 | 2098 | 6479 | 327 |
| realism | 3901 | 1454 | 7209 | 440 |
| romanticism | 3693 | 2433 | 6335 | 543 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 61.41% |
| realism | 57.20% |
| romanticism | 59.25% |
| **Mean** | **59.29%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `42` |
| Type | `rbf` |
| Alpha | `0.001` |
| Epochs | `100` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `30345` |
| Total samples Test | `13004` |
| Limit per category | `-1` |
| Train positive ratio | `désactivé (-1)` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 10331 | 4427 |
| realism | 10130 | 4341 |
| romanticism | 9884 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 10331 | 10130 | 9884 | **30345** |
| **realism** | 10331 | 10130 | 9884 | **30345** |
| **romanticism** | 10331 | 10130 | 9884 | **30345** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\rbf\2026-07-16\10-09-43_058452\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `rbf__impressionism__2026-07-16_10-32-27_378.bin` | 0.75 MB |
| realism | `rbf__realism__2026-07-16_10-32-27_378.bin` | 0.75 MB |
| romanticism | `rbf__romanticism__2026-07-16_10-32-27_378.bin` | 0.75 MB |

Total size: `2.25 MB`


---

