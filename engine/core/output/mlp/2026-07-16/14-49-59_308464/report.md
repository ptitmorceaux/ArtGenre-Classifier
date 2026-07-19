# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 43.63% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 65.18% | 59.50% | 41.72% | 77.29% | 22.71% | 58.28% |
| realism | 59.16% | 55.29% | 43.63% | 66.94% | 33.06% | 56.37% |
| romanticism | 62.93% | 58.46% | 45.63% | 71.28% | 28.72% | 54.37% |
| **Mean** | **62.42%** | **57.75%** | **43.66%** | **71.84%** | **28.16%** | **56.34%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1847 | 6629 | 1948 | 2580 |
| realism | 1894 | 5799 | 2864 | 2447 |
| romanticism | 1933 | 6250 | 2518 | 2303 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 67.31% | 56.68% | 23.36% | 90.00% | 10.00% | 76.64% |
| realism | 64.95% | 52.33% | 14.37% | 90.29% | 9.71% | 85.63% |
| romanticism | 67.29% | 54.95% | 19.52% | 90.37% | 9.63% | 80.48% |
| **Mean** | **66.52%** | **54.65%** | **19.08%** | **90.22%** | **9.78%** | **80.92%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1034 | 7719 | 858 | 3393 |
| realism | 624 | 7822 | 841 | 3717 |
| romanticism | 827 | 7924 | 844 | 3409 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 81.44% |
| realism | 77.76% |
| romanticism | 79.25% |
| **Mean** | **79.48%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1337` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `25` |
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
| Confusion Matrix | `engine\core\output\mlp\2026-07-16\14-49-59_308464\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-16_14-51-56_942.bin` | 0.26 MB |
| realism | `mlp__realism__2026-07-16_14-51-56_942.bin` | 0.26 MB |
| romanticism | `mlp__romanticism__2026-07-16_14-51-56_942.bin` | 0.26 MB |

Total size: `0.78 MB`


---

