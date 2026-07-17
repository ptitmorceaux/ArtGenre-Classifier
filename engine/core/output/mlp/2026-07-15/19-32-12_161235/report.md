# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 45.98% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 65.64% | 62.59% | 53.02% | 72.16% | 27.84% | 46.98% |
| realism | 61.52% | 56.75% | 42.39% | 71.11% | 28.89% | 57.61% |
| romanticism | 64.80% | 58.98% | 42.30% | 75.66% | 24.34% | 57.70% |
| **Mean** | **63.99%** | **59.44%** | **45.90%** | **72.98%** | **27.02%** | **54.10%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2347 | 6189 | 2388 | 2080 |
| realism | 1840 | 6160 | 2503 | 2501 |
| romanticism | 1792 | 6634 | 2134 | 2444 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 61.42% | 61.64% | 62.32% | 60.95% | 39.05% | 37.68% |
| realism | 55.66% | 57.33% | 62.36% | 52.30% | 47.70% | 37.64% |
| romanticism | 57.37% | 57.71% | 58.71% | 56.72% | 43.28% | 41.29% |
| **Mean** | **58.15%** | **58.89%** | **61.13%** | **56.66%** | **43.34%** | **38.87%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2759 | 5228 | 3349 | 1668 |
| realism | 2707 | 4531 | 4132 | 1634 |
| romanticism | 2487 | 4973 | 3795 | 1749 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 71.69% |
| realism | 65.45% |
| romanticism | 70.11% |
| **Mean** | **69.09%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `42` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `40` |
| NPL | `[1024, 32, 16, 1]` |


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
| Confusion Matrix | `engine/core/output/mlp/2026-07-15/19-32-12_161235/confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| realism | `mlp__realism__2026-07-15_19-33-31_858.bin` | 0.13 MB |
| romanticism | `mlp__romanticism__2026-07-15_19-33-31_858.bin` | 0.13 MB |
| impressionism | `mlp__impressionism__2026-07-15_19-33-31_858.bin` | 0.13 MB |

Total size: `0.38 MB`


---

