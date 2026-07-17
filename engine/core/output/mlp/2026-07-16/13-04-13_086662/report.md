# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 45.21% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 64.33% | 59.35% | 43.78% | 74.93% | 25.07% | 56.22% |
| realism | 61.27% | 57.07% | 44.41% | 69.72% | 30.28% | 55.59% |
| romanticism | 64.82% | 60.35% | 47.52% | 73.18% | 26.82% | 52.48% |
| **Mean** | **63.47%** | **58.92%** | **45.24%** | **72.61%** | **27.39%** | **54.76%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1938 | 6427 | 2150 | 2489 |
| realism | 1928 | 6040 | 2623 | 2413 |
| romanticism | 2013 | 6416 | 2352 | 2223 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 60.94% | 60.01% | 57.10% | 62.92% | 37.08% | 42.90% |
| realism | 56.34% | 57.12% | 59.46% | 54.78% | 45.22% | 40.54% |
| romanticism | 60.54% | 61.51% | 64.31% | 58.71% | 41.29% | 35.69% |
| **Mean** | **59.27%** | **59.55%** | **60.29%** | **58.81%** | **41.19%** | **39.71%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2528 | 5397 | 3180 | 1899 |
| realism | 2581 | 4746 | 3917 | 1760 |
| romanticism | 2724 | 5148 | 3620 | 1512 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 88.92% |
| realism | 90.12% |
| romanticism | 90.52% |
| **Mean** | **89.85%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `42` |
| Type | `mlp` |
| Alpha | `0.0005` |
| Epochs | `150` |
| NPL | `[1024, 256, 128, 1]` |


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
| Confusion Matrix | `engine/core/output/mlp/2026-07-16/13-04-13_086662/confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-16_13-48-25_538.bin` | 1.13 MB |
| realism | `mlp__realism__2026-07-16_13-48-25_538.bin` | 1.13 MB |
| romanticism | `mlp__romanticism__2026-07-16_13-48-25_538.bin` | 1.13 MB |

Total size: `3.38 MB`


---

