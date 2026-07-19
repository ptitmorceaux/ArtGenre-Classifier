# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 47.97% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 62.00% | 67.30% | 83.89% | 50.71% | 49.29% | 16.11% |
| realism | 66.06% | 55.61% | 24.16% | 87.06% | 12.94% | 75.84% |
| romanticism | 67.87% | 59.33% | 34.82% | 83.84% | 16.16% | 65.18% |
| **Mean** | **65.31%** | **60.75%** | **47.63%** | **73.87%** | **26.13%** | **52.37%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 3714 | 4349 | 4228 | 713 |
| realism | 1049 | 7542 | 1121 | 3292 |
| romanticism | 1475 | 7351 | 1417 | 2761 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 39.58% | 53.95% | 98.96% | 8.93% | 91.07% | 1.04% |
| realism | 38.00% | 51.75% | 93.14% | 10.37% | 89.63% | 6.86% |
| romanticism | 34.02% | 50.60% | 98.18% | 3.02% | 96.98% | 1.82% |
| **Mean** | **37.20%** | **52.10%** | **96.76%** | **7.44%** | **92.56%** | **3.24%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 4381 | 766 | 7811 | 46 |
| realism | 4043 | 898 | 7765 | 298 |
| romanticism | 4159 | 265 | 8503 | 77 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 58.08% |
| realism | 52.59% |
| romanticism | 54.60% |
| **Mean** | **55.09%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `2024` |
| Type | `rbf` |
| Alpha | `0.001` |
| Epochs | `75` |


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
| Confusion Matrix | `engine/core/output/rbf/2026-07-19/23-17-08_524876/confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| romanticism | `rbf__romanticism__2026-07-19_23-18-16_252.bin` | 0.06 MB |
| realism | `rbf__realism__2026-07-19_23-18-16_252.bin` | 0.06 MB |
| impressionism | `rbf__impressionism__2026-07-19_23-18-16_252.bin` | 0.06 MB |

Total size: `0.19 MB`


---

