# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 40.33% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 61.62% | 54.45% | 31.99% | 76.92% | 23.08% | 68.01% |
| realism | 59.40% | 53.46% | 35.57% | 71.35% | 28.65% | 64.43% |
| romanticism | 59.63% | 58.15% | 53.92% | 62.39% | 37.61% | 46.08% |
| **Mean** | **60.22%** | **55.35%** | **40.49%** | **70.22%** | **29.78%** | **59.51%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1416 | 6597 | 1980 | 3011 |
| realism | 1544 | 6181 | 2482 | 2797 |
| romanticism | 2284 | 5470 | 3298 | 1952 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 63.59% | 53.02% | 19.90% | 86.14% | 13.86% | 80.10% |
| realism | 63.85% | 52.27% | 17.44% | 87.11% | 12.89% | 82.56% |
| romanticism | 65.23% | 55.16% | 26.27% | 84.04% | 15.96% | 73.73% |
| **Mean** | **64.22%** | **53.48%** | **21.20%** | **85.76%** | **14.24%** | **78.80%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 881 | 7388 | 1189 | 3546 |
| realism | 757 | 7546 | 1117 | 3584 |
| romanticism | 1113 | 7369 | 1399 | 3123 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 65.01% |
| realism | 65.71% |
| romanticism | 67.09% |
| **Mean** | **65.93%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `42` |
| Type | `linear` |
| Alpha | `0.0001` |
| Epochs | `150` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `19767` |
| Total samples Test | `13004` |
| Limit per category | `9884` |
| Train positive ratio | `0.25` |
| Normalization | `standard` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 6589 | 4427 |
| realism | 6589 | 4341 |
| romanticism | 6589 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 6589 | 9884 | 9884 | **26357** |
| **realism** | 9884 | 6589 | 9884 | **26357** |
| **romanticism** | 9884 | 9884 | 6589 | **26357** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine/core/output/linear/2026-07-19/23-36-11_466482/confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `linear__impressionism__2026-07-19_23-36-26_383.bin` | 0.00 MB |
| realism | `linear__realism__2026-07-19_23-36-26_383.bin` | 0.00 MB |
| romanticism | `linear__romanticism__2026-07-19_23-36-26_383.bin` | 0.00 MB |

Total size: `0.01 MB`


---

