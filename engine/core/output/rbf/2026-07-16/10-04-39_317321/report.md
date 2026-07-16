# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 41.78% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 60.02% | 59.88% | 59.45% | 60.31% | 39.69% | 40.55% |
| realism | 60.50% | 53.43% | 32.16% | 74.70% | 25.30% | 67.84% |
| romanticism | 63.04% | 55.32% | 33.17% | 77.47% | 22.53% | 66.83% |
| **Mean** | **61.19%** | **56.21%** | **41.59%** | **70.83%** | **29.17%** | **58.41%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2632 | 5173 | 3404 | 1795 |
| realism | 1396 | 6471 | 2192 | 2945 |
| romanticism | 1405 | 6793 | 1975 | 2831 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 63.90% | 60.82% | 51.19% | 70.46% | 29.54% | 48.81% |
| realism | 61.47% | 51.46% | 21.35% | 81.57% | 18.43% | 78.65% |
| romanticism | 63.20% | 54.24% | 28.52% | 79.96% | 20.04% | 71.48% |
| **Mean** | **62.86%** | **55.51%** | **33.69%** | **77.33%** | **22.67%** | **66.31%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2266 | 6043 | 2534 | 2161 |
| realism | 927 | 7066 | 1597 | 3414 |
| romanticism | 1208 | 7011 | 1757 | 3028 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 62.40% |
| realism | 58.33% |
| romanticism | 60.73% |
| **Mean** | **60.49%** |


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
| Total samples Train (chargées) | `3000` |
| Total samples Test | `13004` |
| Limit per category | `1000` |
| Train positive ratio | `désactivé (-1)` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 1000 | 4427 |
| realism | 1000 | 4341 |
| romanticism | 1000 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 1000 | 1000 | 1000 | **3000** |
| **realism** | 1000 | 1000 | 1000 | **3000** |
| **romanticism** | 1000 | 1000 | 1000 | **3000** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\rbf\2026-07-16\10-04-39_317321\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `rbf__impressionism__2026-07-16_10-06-42_171.bin` | 1.50 MB |
| realism | `rbf__realism__2026-07-16_10-06-42_171.bin` | 1.50 MB |
| romanticism | `rbf__romanticism__2026-07-16_10-06-42_171.bin` | 1.50 MB |

Total size: `4.50 MB`


---

