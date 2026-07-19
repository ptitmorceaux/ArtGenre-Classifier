# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 45.96% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 65.84% | 60.86% | 45.25% | 76.47% | 23.53% | 54.75% |
| realism | 60.61% | 57.12% | 46.60% | 67.63% | 32.37% | 53.40% |
| romanticism | 65.47% | 60.45% | 46.06% | 74.85% | 25.15% | 53.94% |
| **Mean** | **63.98%** | **59.48%** | **45.97%** | **72.99%** | **27.01%** | **54.03%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2003 | 6559 | 2018 | 2424 |
| realism | 2023 | 5859 | 2804 | 2318 |
| romanticism | 1951 | 6563 | 2205 | 2285 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 66.86% | 58.26% | 31.31% | 85.22% | 14.78% | 68.69% |
| realism | 64.36% | 54.50% | 24.86% | 84.15% | 15.85% | 75.14% |
| romanticism | 67.72% | 57.62% | 28.64% | 86.60% | 13.40% | 71.36% |
| **Mean** | **66.31%** | **56.79%** | **28.27%** | **85.32%** | **14.68%** | **71.73%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1386 | 7309 | 1268 | 3041 |
| realism | 1079 | 7290 | 1373 | 3262 |
| romanticism | 1213 | 7593 | 1175 | 3023 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 89.30% |
| realism | 84.27% |
| romanticism | 85.62% |
| **Mean** | **86.39%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1337` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `50` |
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
| Confusion Matrix | `engine\core\output\mlp\2026-07-16\14-32-26_019769\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-16_14-39-56_216.bin` | 0.26 MB |
| realism | `mlp__realism__2026-07-16_14-39-56_216.bin` | 0.26 MB |
| romanticism | `mlp__romanticism__2026-07-16_14-39-56_216.bin` | 0.26 MB |

Total size: `0.78 MB`


---

