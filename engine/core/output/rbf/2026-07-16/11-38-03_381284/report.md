# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 39.11% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 67.39% | 56.72% | 23.29% | 90.15% | 9.85% | 76.71% |
| realism | 42.31% | 53.83% | 88.50% | 19.16% | 80.84% | 11.50% |
| romanticism | 68.53% | 52.11% | 5.03% | 99.20% | 0.80% | 94.97% |
| **Mean** | **59.41%** | **54.22%** | **38.94%** | **69.50%** | **30.50%** | **61.06%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1031 | 7732 | 845 | 3396 |
| realism | 3842 | 1660 | 7003 | 499 |
| romanticism | 213 | 8698 | 70 | 4023 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 45.86% | 57.74% | 94.96% | 20.51% | 79.49% | 5.04% |
| realism | 37.04% | 51.44% | 94.75% | 8.13% | 91.87% | 5.25% |
| romanticism | 69.02% | 55.67% | 17.35% | 93.99% | 6.01% | 82.65% |
| **Mean** | **50.64%** | **54.95%** | **69.02%** | **40.87%** | **59.13%** | **30.98%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 4204 | 1759 | 6818 | 223 |
| realism | 4113 | 704 | 7959 | 228 |
| romanticism | 735 | 8241 | 527 | 3501 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 58.19% |
| realism | 57.17% |
| romanticism | 59.55% |
| **Mean** | **58.30%** |


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
| Confusion Matrix | `engine\core\output\rbf\2026-07-16\11-38-03_381284\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `rbf__impressionism__2026-07-16_13-03-54_348.bin` | 3.00 MB |
| realism | `rbf__realism__2026-07-16_13-03-54_348.bin` | 3.00 MB |
| romanticism | `rbf__romanticism__2026-07-16_13-03-54_348.bin` | 3.00 MB |

Total size: `9.00 MB`


---

