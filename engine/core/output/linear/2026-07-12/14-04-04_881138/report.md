# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 36.38% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 58.84% | 53.55% | 37.00% | 70.11% | 29.89% | 63.00% |
| realism | 55.19% | 48.86% | 29.81% | 67.91% | 32.09% | 70.19% |
| romanticism | 58.74% | 54.53% | 42.47% | 66.59% | 33.41% | 57.53% |
| **Mean** | **57.59%** | **52.31%** | **36.43%** | **68.20%** | **31.80%** | **63.57%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1638 | 6013 | 2564 | 2789 |
| realism | 1294 | 5883 | 2780 | 3047 |
| romanticism | 1799 | 5839 | 2929 | 2437 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 57.83% | 53.19% | 38.67% | 67.72% | 32.28% | 61.33% |
| realism | 53.78% | 50.57% | 40.89% | 60.24% | 39.76% | 59.11% |
| romanticism | 55.04% | 52.96% | 47.00% | 58.92% | 41.08% | 53.00% |
| **Mean** | **55.55%** | **52.24%** | **42.19%** | **62.29%** | **37.71%** | **57.81%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1712 | 5808 | 2769 | 2715 |
| realism | 1775 | 5219 | 3444 | 2566 |
| romanticism | 1991 | 5166 | 3602 | 2245 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 100.00% |
| realism | 100.00% |
| romanticism | 100.00% |
| **Mean** | **100.00%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `5678` |
| Type | `linear` |
| Alpha | `0.01` |
| Epochs | `50` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `50` |
| Total samples Test | `13004` |
| Limit per category | `{'impressionism': 56, 'realism': 12, 'romanticism': 32}` |
| Train positive ratio | `0.25` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 15 | 4427 |
| realism | 12 | 4341 |
| romanticism | 23 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 15 | 12 | 32 | **59** |
| **realism** | 18 | 12 | 18 | **48** |
| **romanticism** | 56 | 12 | 23 | **91** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\linear\2026-07-12\14-04-04_881138\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `linear__impressionism__2026-07-12_14-04-05_436.bin` | 0.05 MB |
| realism | `linear__realism__2026-07-12_14-04-05_436.bin` | 0.05 MB |
| romanticism | `linear__romanticism__2026-07-12_14-04-05_436.bin` | 0.05 MB |

Total size: `0.14 MB`


---

