# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 43.66% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 63.03% | 59.65% | 49.09% | 70.22% | 29.78% | 50.91% |
| realism | 60.09% | 57.39% | 49.25% | 65.52% | 34.48% | 50.75% |
| romanticism | 64.20% | 55.94% | 32.25% | 79.63% | 20.37% | 67.75% |
| **Mean** | **62.44%** | **57.66%** | **43.53%** | **71.79%** | **28.21%** | **56.47%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2173 | 6023 | 2554 | 2254 |
| realism | 2138 | 5676 | 2987 | 2203 |
| romanticism | 1366 | 6982 | 1786 | 2870 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 60.35% | 59.25% | 55.79% | 62.70% | 37.30% | 44.21% |
| realism | 58.24% | 56.67% | 51.97% | 61.38% | 38.62% | 48.03% |
| romanticism | 61.56% | 57.41% | 45.49% | 69.32% | 30.68% | 54.51% |
| **Mean** | **60.05%** | **57.78%** | **51.08%** | **64.47%** | **35.53%** | **48.92%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2470 | 5378 | 3199 | 1957 |
| realism | 2256 | 5317 | 3346 | 2085 |
| romanticism | 1927 | 6078 | 2690 | 2309 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 69.24% |
| realism | 66.38% |
| romanticism | 69.29% |
| **Mean** | **68.30%** |


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
| Confusion Matrix | `engine\core\output\linear\2026-07-14\20-47-40_181637\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `linear__impressionism__2026-07-14_20-51-04_803.bin` | 0.05 MB |
| realism | `linear__realism__2026-07-14_20-51-04_803.bin` | 0.05 MB |
| romanticism | `linear__romanticism__2026-07-14_20-51-04_803.bin` | 0.05 MB |

Total size: `0.14 MB`


---

