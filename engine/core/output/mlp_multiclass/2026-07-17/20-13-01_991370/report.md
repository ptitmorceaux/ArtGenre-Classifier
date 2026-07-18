# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 46.36% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 69.54% | 63.10% | 42.92% | 83.28% | 16.72% | 57.08% |
| realism | 64.21% | 56.32% | 32.57% | 80.06% | 19.94% | 67.43% |
| romanticism | 58.97% | 60.30% | 64.09% | 56.50% | 43.50% | 35.91% |
| **Mean** | **64.24%** | **59.91%** | **46.53%** | **73.28%** | **26.72%** | **53.47%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1900 | 7143 | 1434 | 2527 |
| realism | 1414 | 6936 | 1727 | 2927 |
| romanticism | 2715 | 4954 | 3814 | 1521 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| multiclass | 54.00% |
| **Mean** | **54.00%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1337` |
| Type | `mlp_multiclass` |
| Alpha | `0.001` |
| Epochs | `40` |
| NPL | `[12288, 256, 256, 3]` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `29652` |
| Total samples Test | `13004` |
| Limit per category | `9884` |
| Train positive ratio | `0.25` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 9884 | 4427 |
| realism | 9884 | 4341 |
| romanticism | 9884 | 4236 |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\mlp_multiclass\2026-07-17\20-13-01_991370\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| multiclass | `mlp_multiclass__multiclass__2026-07-18_00-15-51_790.bin` | 12.25 MB |

Total size: `12.25 MB`


---

