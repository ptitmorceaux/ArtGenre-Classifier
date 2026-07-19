# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 47.92% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 63.42% | 67.38% | 79.81% | 54.96% | 45.04% | 20.19% |
| realism | 65.48% | 57.12% | 31.95% | 82.28% | 17.72% | 68.05% |
| romanticism | 66.93% | 57.63% | 30.95% | 84.32% | 15.68% | 69.05% |
| **Mean** | **65.28%** | **60.71%** | **47.57%** | **73.85%** | **26.15%** | **52.43%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 3533 | 4714 | 3863 | 894 |
| realism | 1387 | 7128 | 1535 | 2954 |
| romanticism | 1311 | 7393 | 1375 | 2925 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 40.88% | 54.87% | 98.69% | 11.04% | 88.96% | 1.31% |
| realism | 37.56% | 51.98% | 95.39% | 8.58% | 91.42% | 4.61% |
| romanticism | 32.82% | 50.10% | 99.69% | 0.51% | 99.49% | 0.31% |
| **Mean** | **37.09%** | **52.32%** | **97.93%** | **6.71%** | **93.29%** | **2.07%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 4369 | 947 | 7630 | 58 |
| realism | 4141 | 743 | 7920 | 200 |
| romanticism | 4223 | 45 | 8723 | 13 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 58.21% |
| realism | 51.95% |
| romanticism | 54.67% |
| **Mean** | **54.94%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `2024` |
| Type | `rbf` |
| Alpha | `0.001` |
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
| Confusion Matrix | `engine/core/output/rbf/2026-07-19/23-21-36_502089/confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| realism | `rbf__realism__2026-07-19_23-22-44_144.bin` | 0.06 MB |
| romanticism | `rbf__romanticism__2026-07-19_23-22-44_144.bin` | 0.06 MB |
| impressionism | `rbf__impressionism__2026-07-19_23-22-44_144.bin` | 0.06 MB |

Total size: `0.19 MB`


---

