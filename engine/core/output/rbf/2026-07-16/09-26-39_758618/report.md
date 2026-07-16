# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 39.56% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 58.77% | 57.40% | 53.11% | 61.70% | 38.30% | 46.89% |
| realism | 60.38% | 51.90% | 26.38% | 77.42% | 22.58% | 73.62% |
| romanticism | 59.96% | 54.52% | 38.90% | 70.13% | 29.87% | 61.10% |
| **Mean** | **59.70%** | **54.61%** | **39.46%** | **69.75%** | **30.25%** | **60.54%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2351 | 5292 | 3285 | 2076 |
| realism | 1145 | 6707 | 1956 | 3196 |
| romanticism | 1648 | 6149 | 2619 | 2588 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 61.23% | 53.99% | 31.33% | 76.66% | 23.34% | 68.67% |
| realism | 62.30% | 51.35% | 18.41% | 84.29% | 15.71% | 81.59% |
| romanticism | 62.75% | 53.35% | 26.37% | 80.33% | 19.67% | 73.63% |
| **Mean** | **62.09%** | **52.90%** | **25.37%** | **80.42%** | **19.58%** | **74.63%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1387 | 6575 | 2002 | 3040 |
| realism | 799 | 7302 | 1361 | 3542 |
| romanticism | 1117 | 7043 | 1725 | 3119 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 59.47% |
| realism | 56.80% |
| romanticism | 59.47% |
| **Mean** | **58.58%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1337` |
| Type | `rbf` |
| Alpha | `0.001` |
| Epochs | `100` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `3000` |
| Total samples Test | `13004` |
| Limit per category | `1000` |
| Train positive ratio | `désactivé (-1)` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 1000 | 4427 |
| realism | 1000 | 4341 |
| romanticism | 1000 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 1000 | 1000 | 1000 | **3000** |
| **realism** | 1000 | 1000 | 1000 | **3000** |
| **romanticism** | 1000 | 1000 | 1000 | **3000** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\rbf\2026-07-16\09-26-39_758618\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `rbf__impressionism__2026-07-16_09-30-39_842.bin` | 3.00 MB |
| realism | `rbf__realism__2026-07-16_09-30-39_842.bin` | 3.00 MB |
| romanticism | `rbf__romanticism__2026-07-16_09-30-39_842.bin` | 3.00 MB |

Total size: `9.00 MB`


---

