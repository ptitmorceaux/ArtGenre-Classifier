# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 42.16% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 61.74% | 60.63% | 57.13% | 64.12% | 35.88% | 42.87% |
| realism | 62.87% | 52.79% | 22.44% | 83.14% | 16.86% | 77.56% |
| romanticism | 59.70% | 56.34% | 46.72% | 65.97% | 34.03% | 53.28% |
| **Mean** | **61.44%** | **56.58%** | **42.09%** | **71.08%** | **28.92%** | **57.91%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2529 | 5500 | 3077 | 1898 |
| realism | 974 | 7202 | 1461 | 3367 |
| romanticism | 1979 | 5784 | 2984 | 2257 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 54.58% | 58.05% | 68.90% | 47.20% | 52.80% | 31.10% |
| realism | 45.16% | 55.87% | 88.09% | 23.65% | 76.35% | 11.91% |
| romanticism | 55.47% | 57.39% | 62.91% | 51.87% | 48.13% | 37.09% |
| **Mean** | **51.74%** | **57.10%** | **73.30%** | **40.91%** | **59.09%** | **26.70%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 3050 | 4048 | 4529 | 1377 |
| realism | 3824 | 2049 | 6614 | 517 |
| romanticism | 2665 | 4548 | 4220 | 1571 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 59.74% |
| realism | 52.57% |
| romanticism | 56.66% |
| **Mean** | **56.32%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `2024` |
| Type | `rbf` |
| Alpha | `0.0001` |
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
| Confusion Matrix | `engine/core/output/rbf/2026-07-19/22-59-37_538125/confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| realism | `rbf__realism__2026-07-19_23-01-03_845.bin` | 0.08 MB |
| romanticism | `rbf__romanticism__2026-07-19_23-01-03_845.bin` | 0.08 MB |
| impressionism | `rbf__impressionism__2026-07-19_23-01-03_845.bin` | 0.08 MB |

Total size: `0.23 MB`


---

