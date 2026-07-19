# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 50.12% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 68.16% | 63.17% | 47.55% | 78.79% | 21.21% | 52.45% |
| realism | 64.22% | 60.05% | 47.50% | 72.60% | 27.40% | 52.50% |
| romanticism | 67.87% | 64.67% | 55.50% | 73.85% | 26.15% | 44.50% |
| **Mean** | **66.75%** | **62.63%** | **50.18%** | **75.08%** | **24.92%** | **49.82%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2105 | 6758 | 1819 | 2322 |
| realism | 2062 | 6289 | 2374 | 2279 |
| romanticism | 2351 | 6475 | 2293 | 1885 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| multiclass | 78.93% |
| **Mean** | **78.93%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `42` |
| Type | `mlp_multiclass` |
| Alpha | `0.0005` |
| Epochs | `150` |
| NPL | `[1024, 1024, 512, 3]` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `29652` |
| Total samples Test | `13004` |
| Limit per category | `9884` |
| Train positive ratio | `0.50` |
| Normalization | `standard` |

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
| Confusion Matrix | `engine/core/output/mlp_multiclass/2026-07-19/19-35-15_761267/confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| multiclass | `mlp_multiclass__multiclass__2026-07-19_21-31-38_146.bin` | 6.01 MB |

Total size: `6.01 MB`


---

