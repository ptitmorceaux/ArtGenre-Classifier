# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 44.49% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 64.96% | 60.88% | 48.11% | 73.65% | 26.35% | 51.89% |
| realism | 60.72% | 55.54% | 39.94% | 71.13% | 28.87% | 60.06% |
| romanticism | 63.31% | 58.68% | 45.37% | 71.98% | 28.02% | 54.63% |
| **Mean** | **63.00%** | **58.36%** | **44.48%** | **72.25%** | **27.75%** | **55.52%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2130 | 6317 | 2260 | 2297 |
| realism | 1734 | 6162 | 2501 | 2607 |
| romanticism | 1922 | 6311 | 2457 | 2314 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| multiclass | 60.84% |
| **Mean** | **60.84%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `5678` |
| Type | `mlp_multiclass` |
| Alpha | `0.001` |
| Epochs | `30` |
| NPL | `[12288, 64, 32, 3]` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `18000` |
| Total samples Test | `13004` |
| Limit per category | `6000` |
| Train positive ratio | `0.25` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 6000 | 4427 |
| realism | 6000 | 4341 |
| romanticism | 6000 | 4236 |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\mlp_multiclass\2026-07-16\15-45-51_971534\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| multiclass | `mlp_multiclass__multiclass__2026-07-16_15-55-51_866.bin` | 3.01 MB |

Total size: `3.01 MB`


---

