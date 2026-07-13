# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 42.02% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 63.66% | 58.90% | 44.00% | 73.80% | 26.20% | 56.00% |
| realism | 59.01% | 54.64% | 41.47% | 67.81% | 32.19% | 58.53% |
| romanticism | 61.37% | 55.98% | 40.51% | 71.44% | 28.56% | 59.49% |
| **Mean** | **61.35%** | **56.50%** | **41.99%** | **71.02%** | **28.98%** | **58.01%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1948 | 6330 | 2247 | 2479 |
| realism | 1800 | 5874 | 2789 | 2541 |
| romanticism | 1716 | 6264 | 2504 | 2520 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 62.03% | 55.95% | 36.91% | 74.99% | 25.01% | 63.09% |
| realism | 57.99% | 54.44% | 43.75% | 65.13% | 34.87% | 56.25% |
| romanticism | 61.70% | 56.50% | 41.57% | 71.43% | 28.57% | 58.43% |
| **Mean** | **60.57%** | **55.63%** | **40.74%** | **70.52%** | **29.48%** | **59.26%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1634 | 6432 | 2145 | 2793 |
| realism | 1899 | 5642 | 3021 | 2442 |
| romanticism | 1761 | 6263 | 2505 | 2475 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 80.83% |
| realism | 76.86% |
| romanticism | 79.08% |
| **Mean** | **78.92%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `5678` |
| Type | `linear` |
| Alpha | `0.001` |
| Epochs | `100` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `9000` |
| Total samples Test | `13004` |
| Limit per category | `3000` |
| Train positive ratio | `0.33` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 3000 | 4427 |
| realism | 3000 | 4341 |
| romanticism | 3000 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 3000 | 3000 | 3000 | **9000** |
| **realism** | 3000 | 3000 | 3000 | **9000** |
| **romanticism** | 3000 | 3000 | 3000 | **9000** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\linear\2026-07-11\23-37-32_627775\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `linear__impressionism__2026-07-11_23-38-14_906.bin` | 0.05 MB |
| realism | `linear__realism__2026-07-11_23-38-14_906.bin` | 0.05 MB |
| romanticism | `linear__romanticism__2026-07-11_23-38-14_906.bin` | 0.05 MB |

Total size: `0.14 MB`


---

