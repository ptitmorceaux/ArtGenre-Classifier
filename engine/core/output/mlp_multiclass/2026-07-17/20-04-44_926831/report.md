# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 47.67% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 67.56% | 62.42% | 46.31% | 78.54% | 21.46% | 53.69% |
| realism | 62.68% | 59.38% | 49.46% | 69.31% | 30.69% | 50.54% |
| romanticism | 65.10% | 60.49% | 47.26% | 73.71% | 26.29% | 52.74% |
| **Mean** | **65.11%** | **60.76%** | **47.68%** | **73.85%** | **26.15%** | **52.32%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2050 | 6736 | 1841 | 2377 |
| realism | 2147 | 6004 | 2659 | 2194 |
| romanticism | 2002 | 6463 | 2305 | 2234 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| multiclass | 77.88% |
| **Mean** | **77.88%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `42` |
| Type | `mlp_multiclass` |
| Alpha | `0.001` |
| Epochs | `100` |
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
| Confusion Matrix | `engine\core\output\mlp_multiclass\2026-07-17\20-04-44_926831\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| multiclass | `mlp_multiclass__multiclass__2026-07-18_05-25-31_921.bin` | 12.25 MB |

Total size: `12.25 MB`


---

