# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 45.84% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 57.21% | 64.61% | 87.78% | 41.44% | 58.56% | 12.22% |
| realism | 66.83% | 53.33% | 12.74% | 93.93% | 6.07% | 87.26% |
| romanticism | 67.64% | 59.45% | 35.93% | 82.96% | 17.04% | 64.07% |
| **Mean** | **63.89%** | **59.13%** | **45.48%** | **72.78%** | **27.22%** | **54.52%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 3886 | 3554 | 5023 | 541 |
| realism | 553 | 8137 | 526 | 3788 |
| romanticism | 1522 | 7274 | 1494 | 2714 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 38.47% | 53.20% | 99.34% | 7.05% | 92.95% | 0.66% |
| realism | 38.65% | 52.28% | 93.27% | 11.28% | 88.72% | 6.73% |
| romanticism | 33.04% | 50.20% | 99.41% | 0.98% | 99.02% | 0.59% |
| **Mean** | **36.72%** | **51.89%** | **97.34%** | **6.44%** | **93.56%** | **2.66%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 4398 | 605 | 7972 | 29 |
| realism | 4049 | 977 | 7686 | 292 |
| romanticism | 4211 | 86 | 8682 | 25 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 58.31% |
| realism | 52.41% |
| romanticism | 54.94% |
| **Mean** | **55.22%** |


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
| Confusion Matrix | `engine/core/output/rbf/2026-07-19/23-03-19_062903/confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| realism | `rbf__realism__2026-07-19_23-04-26_724.bin` | 0.06 MB |
| impressionism | `rbf__impressionism__2026-07-19_23-04-26_724.bin` | 0.06 MB |
| romanticism | `rbf__romanticism__2026-07-19_23-04-26_724.bin` | 0.06 MB |

Total size: `0.19 MB`


---

