# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 49.53% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 68.44% | 64.05% | 50.30% | 77.80% | 22.20% | 49.70% |
| realism | 62.93% | 60.31% | 52.41% | 68.21% | 31.79% | 47.59% |
| romanticism | 67.69% | 62.02% | 45.77% | 78.27% | 21.73% | 54.23% |
| **Mean** | **66.35%** | **62.13%** | **49.50%** | **74.76%** | **25.24%** | **50.50%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2227 | 6673 | 1904 | 2200 |
| realism | 2275 | 5909 | 2754 | 2066 |
| romanticism | 1939 | 6863 | 1905 | 2297 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 69.91% | 61.66% | 35.83% | 87.50% | 12.50% | 64.17% |
| realism | 66.20% | 56.53% | 27.44% | 85.62% | 14.38% | 72.56% |
| romanticism | 69.23% | 58.80% | 28.87% | 88.73% | 11.27% | 71.13% |
| **Mean** | **68.45%** | **59.00%** | **30.71%** | **87.28%** | **12.72%** | **69.29%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1586 | 7505 | 1072 | 2841 |
| realism | 1191 | 7417 | 1246 | 3150 |
| romanticism | 1223 | 7780 | 988 | 3013 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 88.68% |
| realism | 86.63% |
| romanticism | 85.98% |
| **Mean** | **87.10%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1337` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `100` |
| NPL | `[12288, 256, 256, 1]` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `20229` |
| Total samples Test | `13004` |
| Limit per category | `-1` |
| Train positive ratio | `0.25` |
| Normalization | `per_column` |

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
| Confusion Matrix | `engine\core\output\mlp\2026-07-13\17-06-45_581095\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-14_13-42-26_355.bin` | 12.25 MB |
| realism | `mlp__realism__2026-07-14_13-42-26_355.bin` | 12.25 MB |
| romanticism | `mlp__romanticism__2026-07-14_13-42-26_355.bin` | 12.25 MB |

Total size: `36.76 MB`


---

