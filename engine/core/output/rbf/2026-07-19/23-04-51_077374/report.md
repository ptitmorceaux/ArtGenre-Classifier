# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 44.59% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 53.78% | 62.98% | 91.82% | 34.14% | 65.86% | 8.18% |
| realism | 66.78% | 54.17% | 16.24% | 92.10% | 7.90% | 83.76% |
| romanticism | 68.62% | 57.16% | 24.27% | 90.04% | 9.96% | 75.73% |
| **Mean** | **63.06%** | **58.10%** | **44.11%** | **72.10%** | **27.90%** | **55.89%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 4065 | 2928 | 5649 | 362 |
| realism | 705 | 7979 | 684 | 3636 |
| romanticism | 1028 | 7895 | 873 | 3208 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 40.02% | 54.29% | 99.01% | 9.57% | 90.43% | 0.99% |
| realism | 40.35% | 53.47% | 92.95% | 13.99% | 86.01% | 7.05% |
| romanticism | 34.07% | 50.75% | 98.63% | 2.87% | 97.13% | 1.37% |
| **Mean** | **38.14%** | **52.84%** | **96.86%** | **8.81%** | **91.19%** | **3.14%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 4383 | 821 | 7756 | 44 |
| realism | 4035 | 1212 | 7451 | 306 |
| romanticism | 4178 | 252 | 8516 | 58 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 58.47% |
| realism | 52.15% |
| romanticism | 54.84% |
| **Mean** | **55.15%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `2024` |
| Type | `rbf` |
| Alpha | `0.0001` |
| Epochs | `200` |


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
| Confusion Matrix | `engine/core/output/rbf/2026-07-19/23-04-51_077374/confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| romanticism | `rbf__romanticism__2026-07-19_23-05-59_404.bin` | 0.06 MB |
| realism | `rbf__realism__2026-07-19_23-05-59_404.bin` | 0.06 MB |
| impressionism | `rbf__impressionism__2026-07-19_23-05-59_404.bin` | 0.06 MB |

Total size: `0.19 MB`


---

