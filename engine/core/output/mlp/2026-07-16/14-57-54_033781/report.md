# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 44.29% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 64.85% | 60.61% | 47.32% | 73.90% | 26.10% | 52.68% |
| realism | 60.86% | 56.27% | 42.46% | 70.08% | 29.92% | 57.54% |
| romanticism | 62.87% | 57.73% | 42.99% | 72.47% | 27.53% | 57.01% |
| **Mean** | **62.86%** | **58.20%** | **44.26%** | **72.15%** | **27.85%** | **55.74%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2095 | 6338 | 2239 | 2332 |
| realism | 1843 | 6071 | 2592 | 2498 |
| romanticism | 1821 | 6354 | 2414 | 2415 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 67.54% | 55.98% | 19.74% | 92.21% | 7.79% | 80.26% |
| realism | 66.56% | 52.28% | 9.33% | 95.23% | 4.77% | 90.67% |
| romanticism | 67.42% | 53.06% | 11.85% | 94.26% | 5.74% | 88.15% |
| **Mean** | **67.17%** | **53.77%** | **13.64%** | **93.90%** | **6.10%** | **86.36%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 874 | 7909 | 668 | 3553 |
| realism | 405 | 8250 | 413 | 3936 |
| romanticism | 502 | 8265 | 503 | 3734 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 77.89% |
| realism | 76.04% |
| romanticism | 77.33% |
| **Mean** | **77.09%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1337` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `15` |
| NPL | `[1024, 64, 32, 1]` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `20229` |
| Total samples Test | `13004` |
| Limit per category | `-1` |
| Train positive ratio | `0.25` |
| Normalization | `standard` |

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
| Confusion Matrix | `engine\core\output\mlp\2026-07-16\14-57-54_033781\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-16_14-58-59_438.bin` | 0.26 MB |
| realism | `mlp__realism__2026-07-16_14-58-59_438.bin` | 0.26 MB |
| romanticism | `mlp__romanticism__2026-07-16_14-58-59_438.bin` | 0.26 MB |

Total size: `0.78 MB`


---

