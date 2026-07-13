# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 37.00% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 61.61% | 54.99% | 34.24% | 75.74% | 24.26% | 65.76% |
| realism | 53.78% | 49.63% | 37.13% | 62.13% | 37.87% | 62.87% |
| romanticism | 58.60% | 53.72% | 39.73% | 67.71% | 32.29% | 60.27% |
| **Mean** | **58.00%** | **52.78%** | **37.04%** | **68.53%** | **31.47%** | **62.96%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1516 | 6496 | 2081 | 2911 |
| realism | 1612 | 5382 | 3281 | 2729 |
| romanticism | 1683 | 5937 | 2831 | 2553 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 56.93% | 53.97% | 44.68% | 63.25% | 36.75% | 55.32% |
| realism | 51.37% | 50.92% | 49.55% | 52.28% | 47.72% | 50.45% |
| romanticism | 55.35% | 53.13% | 46.74% | 59.51% | 40.49% | 53.26% |
| **Mean** | **54.55%** | **52.67%** | **46.99%** | **58.35%** | **41.65%** | **53.01%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1978 | 5425 | 3152 | 2449 |
| realism | 2151 | 4529 | 4134 | 2190 |
| romanticism | 1980 | 5218 | 3550 | 2256 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 93.75% |
| realism | 81.25% |
| romanticism | 87.50% |
| **Mean** | **87.50%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `2024` |
| Type | `linear` |
| Alpha | `0.001` |
| Epochs | `10` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `12` |
| Total samples Test | `13004` |
| Limit per category | `6` |
| Train positive ratio | `0.25` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 4 | 4427 |
| realism | 4 | 4341 |
| romanticism | 4 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 4 | 6 | 6 | **16** |
| **realism** | 6 | 4 | 6 | **16** |
| **romanticism** | 6 | 6 | 4 | **16** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\linear\2026-07-12\03-05-29_191835\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `linear__impressionism__2026-07-12_03-05-30_069.bin` | 0.05 MB |
| realism | `linear__realism__2026-07-12_03-05-30_069.bin` | 0.05 MB |
| romanticism | `linear__romanticism__2026-07-12_03-05-30_069.bin` | 0.05 MB |

Total size: `0.14 MB`


---

