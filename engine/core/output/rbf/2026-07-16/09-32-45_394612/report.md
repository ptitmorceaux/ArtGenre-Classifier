# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 32.97% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 63.43% | 50.06% | 8.18% | 91.94% | 8.06% | 91.82% |
| realism | 35.74% | 48.66% | 87.54% | 9.78% | 90.22% | 12.46% |
| romanticism | 66.77% | 50.28% | 2.95% | 97.60% | 2.40% | 97.05% |
| **Mean** | **55.31%** | **49.67%** | **32.89%** | **66.44%** | **33.56%** | **67.11%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 362 | 7886 | 691 | 4065 |
| realism | 3800 | 847 | 7816 | 541 |
| romanticism | 125 | 8558 | 210 | 4111 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 40.35% | 53.26% | 93.72% | 12.80% | 87.20% | 6.28% |
| realism | 33.92% | 49.27% | 95.46% | 3.08% | 96.92% | 4.54% |
| romanticism | 65.43% | 49.85% | 5.15% | 94.55% | 5.45% | 94.85% |
| **Mean** | **46.57%** | **50.79%** | **64.78%** | **36.81%** | **63.19%** | **35.22%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 4149 | 1098 | 7479 | 278 |
| realism | 4144 | 267 | 8396 | 197 |
| romanticism | 218 | 8290 | 478 | 4018 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 57.53% |
| realism | 56.80% |
| romanticism | 57.20% |
| **Mean** | **57.18%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `5678` |
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
| Confusion Matrix | `engine\core\output\rbf\2026-07-16\09-32-45_394612\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `rbf__impressionism__2026-07-16_09-38-25_167.bin` | 12.00 MB |
| realism | `rbf__realism__2026-07-16_09-38-25_167.bin` | 12.00 MB |
| romanticism | `rbf__romanticism__2026-07-16_09-38-25_167.bin` | 12.00 MB |

Total size: `36.00 MB`


---

