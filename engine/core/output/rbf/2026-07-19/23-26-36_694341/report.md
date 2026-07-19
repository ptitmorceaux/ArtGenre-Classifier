# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 45.06% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 61.90% | 66.57% | 81.21% | 51.93% | 48.07% | 18.79% |
| realism | 60.33% | 57.90% | 50.59% | 65.21% | 34.79% | 49.41% |
| romanticism | 67.89% | 50.76% | 1.61% | 99.91% | 0.09% | 98.39% |
| **Mean** | **63.37%** | **58.41%** | **44.47%** | **72.35%** | **27.65%** | **55.53%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 3595 | 4454 | 4123 | 832 |
| realism | 2196 | 5649 | 3014 | 2145 |
| romanticism | 68 | 8760 | 8 | 4168 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 41.29% | 55.15% | 98.55% | 11.74% | 88.26% | 1.45% |
| realism | 36.47% | 51.49% | 96.71% | 6.28% | 93.72% | 3.29% |
| romanticism | 63.09% | 60.30% | 52.31% | 68.29% | 31.71% | 47.69% |
| **Mean** | **46.95%** | **55.65%** | **82.52%** | **28.77%** | **71.23%** | **17.48%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 4363 | 1007 | 7570 | 64 |
| realism | 4198 | 544 | 8119 | 143 |
| romanticism | 2216 | 5988 | 2780 | 2020 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 57.77% |
| realism | 52.73% |
| romanticism | 55.19% |
| **Mean** | **55.23%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `2024` |
| Type | `rbf` |
| Alpha | `0.01` |
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
| Confusion Matrix | `engine/core/output/rbf/2026-07-19/23-26-36_694341/confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| romanticism | `rbf__romanticism__2026-07-19_23-27-45_463.bin` | 0.06 MB |
| realism | `rbf__realism__2026-07-19_23-27-45_463.bin` | 0.06 MB |
| impressionism | `rbf__impressionism__2026-07-19_23-27-45_463.bin` | 0.06 MB |

Total size: `0.19 MB`


---

