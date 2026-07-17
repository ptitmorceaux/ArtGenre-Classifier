# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 44.52% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 64.35% | 60.43% | 48.16% | 72.71% | 27.29% | 51.84% |
| realism | 60.54% | 56.60% | 44.74% | 68.46% | 31.54% | 55.26% |
| romanticism | 64.16% | 58.05% | 40.51% | 75.58% | 24.42% | 59.49% |
| **Mean** | **63.02%** | **58.36%** | **44.47%** | **72.25%** | **27.75%** | **55.53%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2132 | 6236 | 2341 | 2295 |
| realism | 1942 | 5931 | 2732 | 2399 |
| romanticism | 1716 | 6627 | 2141 | 2520 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 66.88% | 55.71% | 20.69% | 90.72% | 9.28% | 79.31% |
| realism | 66.01% | 52.79% | 13.02% | 92.57% | 7.43% | 86.98% |
| romanticism | 67.07% | 54.09% | 16.86% | 91.33% | 8.67% | 83.14% |
| **Mean** | **66.65%** | **54.20%** | **16.85%** | **91.54%** | **8.46%** | **83.15%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 916 | 7781 | 796 | 3511 |
| realism | 565 | 8019 | 644 | 3776 |
| romanticism | 714 | 8008 | 760 | 3522 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 79.57% |
| realism | 77.05% |
| romanticism | 79.80% |
| **Mean** | **78.81%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1337` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `20` |
| NPL | `[1024, 64, 32, 1]` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `20229` |
| Total samples Test | `13004` |
| Limit per category | `-1` |
| Train positive ratio | `0.25` |
| Normalization | `standard` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 6671 | 4427 |
| realism | 6738 | 4341 |
| romanticism | 6820 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 6671 | 10130 | 9884 | **26685** |
| **realism** | 10331 | 6738 | 9884 | **26953** |
| **romanticism** | 10331 | 10130 | 6820 | **27281** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\mlp\2026-07-16\14-54-27_529411\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-16_14-55-56_859.bin` | 0.26 MB |
| realism | `mlp__realism__2026-07-16_14-55-56_859.bin` | 0.26 MB |
| romanticism | `mlp__romanticism__2026-07-16_14-55-56_859.bin` | 0.26 MB |

Total size: `0.78 MB`


---

