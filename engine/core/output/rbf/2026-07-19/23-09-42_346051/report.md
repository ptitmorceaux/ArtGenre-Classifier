# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 42.76% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 53.44% | 62.67% | 91.62% | 33.73% | 66.27% | 8.38% |
| realism | 64.03% | 56.12% | 32.34% | 79.90% | 20.10% | 67.66% |
| romanticism | 68.06% | 51.09% | 2.38% | 99.79% | 0.21% | 97.62% |
| **Mean** | **61.84%** | **56.63%** | **42.12%** | **71.14%** | **28.86%** | **57.88%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 4056 | 2893 | 5684 | 371 |
| realism | 1404 | 6922 | 1741 | 2937 |
| romanticism | 101 | 8750 | 18 | 4135 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 40.02% | 54.23% | 98.78% | 9.69% | 90.31% | 1.22% |
| realism | 39.09% | 52.74% | 93.83% | 11.66% | 88.34% | 6.17% |
| romanticism | 59.27% | 60.07% | 62.37% | 57.78% | 42.22% | 37.63% |
| **Mean** | **46.13%** | **55.68%** | **84.99%** | **26.38%** | **73.62%** | **15.01%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 4373 | 831 | 7746 | 54 |
| realism | 4073 | 1010 | 7653 | 268 |
| romanticism | 2642 | 5066 | 3702 | 1594 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 58.18% |
| realism | 52.46% |
| romanticism | 54.57% |
| **Mean** | **55.07%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `2024` |
| Type | `rbf` |
| Alpha | `0.0001` |
| Epochs | `150` |


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
| Confusion Matrix | `engine/core/output/rbf/2026-07-19/23-09-42_346051/confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `rbf__impressionism__2026-07-19_23-10-39_625.bin` | 0.06 MB |
| romanticism | `rbf__romanticism__2026-07-19_23-10-39_625.bin` | 0.06 MB |
| realism | `rbf__realism__2026-07-19_23-10-39_625.bin` | 0.06 MB |

Total size: `0.18 MB`


---

