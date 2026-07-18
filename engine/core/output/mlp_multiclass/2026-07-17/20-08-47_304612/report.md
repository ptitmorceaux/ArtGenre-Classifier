# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 49.99% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 68.78% | 64.70% | 51.91% | 77.49% | 22.51% | 48.09% |
| realism | 64.42% | 59.32% | 44.00% | 74.65% | 25.35% | 56.00% |
| romanticism | 66.79% | 63.52% | 54.13% | 72.90% | 27.10% | 45.87% |
| **Mean** | **66.66%** | **62.51%** | **50.01%** | **75.01%** | **24.99%** | **49.99%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2298 | 6646 | 1931 | 2129 |
| realism | 1910 | 6467 | 2196 | 2431 |
| romanticism | 2293 | 6392 | 2376 | 1943 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| multiclass | 78.82% |
| **Mean** | **78.82%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1337` |
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
| Confusion Matrix | `engine\core\output\mlp_multiclass\2026-07-17\20-08-47_304612\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| multiclass | `mlp_multiclass__multiclass__2026-07-18_05-08-53_840.bin` | 12.25 MB |

Total size: `12.25 MB`


---

