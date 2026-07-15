# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 46.49% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 65.89% | 60.61% | 44.07% | 77.15% | 22.85% | 55.93% |
| realism | 62.20% | 57.21% | 42.18% | 72.24% | 27.76% | 57.82% |
| romanticism | 64.88% | 61.92% | 53.42% | 70.42% | 29.58% | 46.58% |
| **Mean** | **64.32%** | **59.91%** | **46.56%** | **73.27%** | **26.73%** | **53.44%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1951 | 6617 | 1960 | 2476 |
| realism | 1831 | 6258 | 2405 | 2510 |
| romanticism | 2263 | 6174 | 2594 | 1973 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 64.88% | 56.71% | 31.13% | 82.30% | 17.70% | 68.87% |
| realism | 63.75% | 56.47% | 34.55% | 78.38% | 21.62% | 65.45% |
| romanticism | 65.94% | 61.05% | 47.03% | 75.08% | 24.92% | 52.97% |
| **Mean** | **64.86%** | **58.08%** | **37.57%** | **78.59%** | **21.41%** | **62.43%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1378 | 7059 | 1518 | 3049 |
| realism | 1500 | 6790 | 1873 | 2841 |
| romanticism | 1992 | 6583 | 2185 | 2244 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 74.62% |
| realism | 72.15% |
| romanticism | 73.52% |
| **Mean** | **73.43%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1337` |
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
| Confusion Matrix | `engine\core\output\linear\2026-07-14\20-01-36_803290\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `linear__impressionism__2026-07-14_20-05-04_639.bin` | 0.05 MB |
| realism | `linear__realism__2026-07-14_20-05-04_639.bin` | 0.05 MB |
| romanticism | `linear__romanticism__2026-07-14_20-05-04_639.bin` | 0.05 MB |

Total size: `0.14 MB`


---

