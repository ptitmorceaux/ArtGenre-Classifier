# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 47.02% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 61.70% | 66.47% | 81.41% | 51.52% | 48.48% | 18.59% |
| realism | 65.40% | 55.71% | 26.56% | 84.86% | 15.14% | 73.44% |
| romanticism | 66.94% | 57.92% | 32.03% | 83.80% | 16.20% | 67.97% |
| **Mean** | **64.68%** | **60.03%** | **46.67%** | **73.39%** | **26.61%** | **53.33%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 3604 | 4419 | 4158 | 823 |
| realism | 1153 | 7351 | 1312 | 3188 |
| romanticism | 1357 | 7348 | 1420 | 2879 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 44.77% | 57.32% | 96.63% | 18.00% | 82.00% | 3.37% |
| realism | 43.70% | 54.30% | 86.18% | 22.42% | 77.58% | 13.82% |
| romanticism | 39.20% | 53.79% | 95.63% | 11.94% | 88.06% | 4.37% |
| **Mean** | **42.56%** | **55.13%** | **92.82%** | **17.45%** | **82.55%** | **7.18%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 4278 | 1544 | 7033 | 149 |
| realism | 3741 | 1942 | 6721 | 600 |
| romanticism | 4051 | 1047 | 7721 | 185 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 57.73% |
| realism | 52.76% |
| romanticism | 54.84% |
| **Mean** | **55.11%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `2024` |
| Type | `rbf` |
| Alpha | `0.001` |
| Epochs | `50` |


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
| Confusion Matrix | `engine/core/output/rbf/2026-07-19/23-19-37_102140/confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `rbf__impressionism__2026-07-19_23-20-44_874.bin` | 0.06 MB |
| realism | `rbf__realism__2026-07-19_23-20-44_874.bin` | 0.06 MB |
| romanticism | `rbf__romanticism__2026-07-19_23-20-44_874.bin` | 0.06 MB |

Total size: `0.19 MB`


---

