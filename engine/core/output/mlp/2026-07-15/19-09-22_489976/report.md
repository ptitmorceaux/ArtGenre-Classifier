# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 45.50% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 64.63% | 59.83% | 44.79% | 74.86% | 25.14% | 55.21% |
| realism | 61.39% | 56.95% | 43.58% | 70.31% | 29.69% | 56.42% |
| romanticism | 64.99% | 60.65% | 48.21% | 73.10% | 26.90% | 51.79% |
| **Mean** | **63.67%** | **59.14%** | **45.53%** | **72.76%** | **27.24%** | **54.47%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1983 | 6421 | 2156 | 2444 |
| realism | 1892 | 6091 | 2572 | 2449 |
| romanticism | 2042 | 6409 | 2359 | 2194 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 60.70% | 59.82% | 57.06% | 62.59% | 37.41% | 42.94% |
| realism | 56.01% | 56.37% | 57.45% | 55.28% | 44.72% | 42.55% |
| romanticism | 60.67% | 61.09% | 62.32% | 59.87% | 40.13% | 37.68% |
| **Mean** | **59.13%** | **59.09%** | **58.94%** | **59.24%** | **40.76%** | **41.06%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2526 | 5368 | 3209 | 1901 |
| realism | 2494 | 4789 | 3874 | 1847 |
| romanticism | 2640 | 5249 | 3519 | 1596 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 93.37% |
| realism | 94.36% |
| romanticism | 93.57% |
| **Mean** | **93.77%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `42` |
| Type | `mlp` |
| Alpha | `0.0005` |
| Epochs | `150` |
| NPL | `[1024, 128, 64, 1]` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `30344` |
| Total samples Test | `13004` |
| Limit per category | `-1` |
| Train positive ratio | `0.50` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 10331 | 4427 |
| realism | 10129 | 4341 |
| romanticism | 9884 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 10331 | 5166 | 5165 | **20662** |
| **realism** | 5065 | 10129 | 5064 | **20258** |
| **romanticism** | 4942 | 4942 | 9884 | **19768** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine/core/output/mlp/2026-07-15/19-09-22_489976/confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-15_19-26-14_074.bin` | 0.53 MB |
| realism | `mlp__realism__2026-07-15_19-26-14_074.bin` | 0.53 MB |
| romanticism | `mlp__romanticism__2026-07-15_19-26-14_074.bin` | 0.53 MB |

Total size: `1.60 MB`


---

