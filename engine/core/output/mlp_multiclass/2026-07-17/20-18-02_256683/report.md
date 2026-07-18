# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 47.26% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 68.44% | 63.42% | 47.71% | 79.14% | 20.86% | 52.29% |
| realism | 60.77% | 57.30% | 46.83% | 67.76% | 32.24% | 53.17% |
| romanticism | 65.31% | 60.64% | 47.24% | 74.04% | 25.96% | 52.76% |
| **Mean** | **64.84%** | **60.45%** | **47.26%** | **73.65%** | **26.35%** | **52.74%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2112 | 6788 | 1789 | 2315 |
| realism | 2033 | 5870 | 2793 | 2308 |
| romanticism | 2001 | 6492 | 2276 | 2235 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| multiclass | 53.00% |
| **Mean** | **53.00%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `42` |
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
| Confusion Matrix | `engine\core\output\mlp_multiclass\2026-07-17\20-18-02_256683\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| multiclass | `mlp_multiclass__multiclass__2026-07-18_00-19-08_416.bin` | 12.25 MB |

Total size: `12.25 MB`


---

