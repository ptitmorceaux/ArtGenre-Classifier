# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 43.43% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 62.38% | 61.12% | 57.17% | 65.07% | 34.93% | 42.83% |
| realism | 62.27% | 55.21% | 33.98% | 76.45% | 23.55% | 66.02% |
| romanticism | 62.20% | 56.13% | 38.74% | 73.53% | 26.47% | 61.26% |
| **Mean** | **62.28%** | **57.49%** | **43.30%** | **71.68%** | **28.32%** | **56.70%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2531 | 5581 | 2996 | 1896 |
| realism | 1475 | 6623 | 2040 | 2866 |
| romanticism | 1641 | 6447 | 2321 | 2595 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| multiclass | 50.06% |
| **Mean** | **50.06%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `2024` |
| Type | `mlp_multiclass` |
| Alpha | `0.001` |
| Epochs | `30` |
| NPL | `[12288, 16, 8, 3]` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `9000` |
| Total samples Test | `13004` |
| Limit per category | `3000` |
| Train positive ratio | `0.25` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 3000 | 4427 |
| realism | 3000 | 4341 |
| romanticism | 3000 | 4236 |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\mlp_multiclass\2026-07-16\15-50-58_270067\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| multiclass | `mlp_multiclass__multiclass__2026-07-16_15-52-34_889.bin` | 0.75 MB |

Total size: `0.75 MB`


---

