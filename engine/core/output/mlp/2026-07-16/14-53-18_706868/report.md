# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 45.09% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 65.40% | 60.27% | 44.23% | 76.32% | 23.68% | 55.77% |
| realism | 60.94% | 56.74% | 44.11% | 69.36% | 30.64% | 55.89% |
| romanticism | 63.86% | 59.50% | 47.00% | 72.00% | 28.00% | 53.00% |
| **Mean** | **63.40%** | **58.84%** | **45.11%** | **72.56%** | **27.44%** | **54.89%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1958 | 6546 | 2031 | 2469 |
| realism | 1915 | 6009 | 2654 | 2426 |
| romanticism | 1991 | 6313 | 2455 | 2245 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 67.46% | 57.54% | 26.45% | 88.63% | 11.37% | 73.55% |
| realism | 64.94% | 53.68% | 19.81% | 87.56% | 12.44% | 80.19% |
| romanticism | 67.06% | 56.54% | 26.35% | 86.72% | 13.28% | 73.65% |
| **Mean** | **66.49%** | **55.92%** | **24.20%** | **87.64%** | **12.36%** | **75.80%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1171 | 7602 | 975 | 3256 |
| realism | 860 | 7585 | 1078 | 3481 |
| romanticism | 1116 | 7604 | 1164 | 3120 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 83.24% |
| realism | 79.88% |
| romanticism | 81.61% |
| **Mean** | **81.58%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1337` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `30` |
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
| Confusion Matrix | `engine\core\output\mlp\2026-07-16\14-53-18_706868\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-16_14-55-34_853.bin` | 0.26 MB |
| realism | `mlp__realism__2026-07-16_14-55-34_853.bin` | 0.26 MB |
| romanticism | `mlp__romanticism__2026-07-16_14-55-34_853.bin` | 0.26 MB |

Total size: `0.78 MB`


---

