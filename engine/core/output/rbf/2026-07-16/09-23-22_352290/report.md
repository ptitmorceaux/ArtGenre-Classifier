# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 43.04% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 69.68% | 61.04% | 33.95% | 88.12% | 11.88% | 66.05% |
| realism | 56.92% | 52.43% | 38.93% | 65.94% | 34.06% | 61.07% |
| romanticism | 59.48% | 58.78% | 56.75% | 60.80% | 39.20% | 43.25% |
| **Mean** | **62.03%** | **57.41%** | **43.21%** | **71.62%** | **28.38%** | **56.79%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1503 | 7558 | 1019 | 2924 |
| realism | 1690 | 5712 | 2951 | 2651 |
| romanticism | 2404 | 5331 | 3437 | 1832 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 67.59% | 53.85% | 10.80% | 96.91% | 3.09% | 89.20% |
| realism | 66.46% | 50.26% | 1.54% | 98.98% | 1.02% | 98.46% |
| romanticism | 64.87% | 53.85% | 22.24% | 85.47% | 14.53% | 77.76% |
| **Mean** | **66.31%** | **52.66%** | **11.53%** | **93.79%** | **6.21%** | **88.47%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 478 | 8312 | 265 | 3949 |
| realism | 67 | 8575 | 88 | 4274 |
| romanticism | 942 | 7494 | 1274 | 3294 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 61.40% |
| realism | 59.33% |
| romanticism | 60.00% |
| **Mean** | **60.24%** |


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
| Confusion Matrix | `engine\core\output\rbf\2026-07-16\09-23-22_352290\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `rbf__impressionism__2026-07-16_09-24-46_350.bin` | 0.75 MB |
| realism | `rbf__realism__2026-07-16_09-24-46_350.bin` | 0.75 MB |
| romanticism | `rbf__romanticism__2026-07-16_09-24-46_350.bin` | 0.75 MB |

Total size: `2.25 MB`


---

