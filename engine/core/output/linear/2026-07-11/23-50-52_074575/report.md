# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 44.10% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 64.54% | 58.98% | 41.54% | 76.41% | 23.59% | 58.46% |
| realism | 60.22% | 55.91% | 42.94% | 68.88% | 31.12% | 57.06% |
| romanticism | 63.44% | 59.44% | 47.97% | 70.92% | 29.08% | 52.03% |
| **Mean** | **62.73%** | **58.11%** | **44.15%** | **72.07%** | **27.93%** | **55.85%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1839 | 6554 | 2023 | 2588 |
| realism | 1864 | 5967 | 2696 | 2477 |
| romanticism | 2032 | 6218 | 2550 | 2204 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 63.62% | 60.04% | 48.84% | 71.25% | 28.75% | 51.16% |
| realism | 56.18% | 53.29% | 44.62% | 61.96% | 38.04% | 55.38% |
| romanticism | 61.87% | 57.80% | 46.10% | 69.49% | 30.51% | 53.90% |
| **Mean** | **60.56%** | **57.04%** | **46.52%** | **67.57%** | **32.43%** | **53.48%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2162 | 6111 | 2466 | 2265 |
| realism | 1937 | 5368 | 3295 | 2404 |
| romanticism | 1953 | 6093 | 2675 | 2283 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 72.76% |
| realism | 69.51% |
| romanticism | 71.91% |
| **Mean** | **71.39%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1337` |
| Type | `linear` |
| Alpha | `0.001` |
| Epochs | `100` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `18000` |
| Total samples Test | `13004` |
| Limit per category | `6000` |
| Train positive ratio | `0.33` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 6000 | 4427 |
| realism | 6000 | 4341 |
| romanticism | 6000 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 6000 | 6000 | 6000 | **18000** |
| **realism** | 6000 | 6000 | 6000 | **18000** |
| **romanticism** | 6000 | 6000 | 6000 | **18000** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\linear\2026-07-11\23-50-52_074575\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `linear__impressionism__2026-07-11_23-53-10_876.bin` | 0.05 MB |
| realism | `linear__realism__2026-07-11_23-53-10_876.bin` | 0.05 MB |
| romanticism | `linear__romanticism__2026-07-11_23-53-10_876.bin` | 0.05 MB |

Total size: `0.14 MB`


---

