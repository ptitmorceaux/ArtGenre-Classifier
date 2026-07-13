# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 36.70% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 60.47% | 51.72% | 24.33% | 79.12% | 20.88% | 75.67% |
| realism | 58.38% | 52.25% | 33.79% | 70.70% | 29.30% | 66.21% |
| romanticism | 54.56% | 54.06% | 52.62% | 55.50% | 44.50% | 47.38% |
| **Mean** | **57.80%** | **52.68%** | **36.91%** | **68.44%** | **31.56%** | **63.09%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1077 | 6786 | 1791 | 3350 |
| realism | 1467 | 6125 | 2538 | 2874 |
| romanticism | 2229 | 4866 | 3902 | 2007 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 56.41% | 51.83% | 37.50% | 66.17% | 33.83% | 62.50% |
| realism | 54.66% | 52.05% | 44.21% | 59.90% | 40.10% | 55.79% |
| romanticism | 50.97% | 52.99% | 58.81% | 47.18% | 52.82% | 41.19% |
| **Mean** | **54.01%** | **52.29%** | **46.84%** | **57.75%** | **42.25%** | **53.16%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1660 | 5675 | 2902 | 2767 |
| realism | 1919 | 5189 | 3474 | 2422 |
| romanticism | 2491 | 4137 | 4631 | 1745 |


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
| Seed | `1337` |
| Type | `linear` |
| Alpha | `0.001` |
| Epochs | `100` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `90` |
| Total samples Test | `13004` |
| Limit per category | `30` |
| Train positive ratio | `0.33` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 30 | 4427 |
| realism | 30 | 4341 |
| romanticism | 30 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 30 | 30 | 30 | **90** |
| **realism** | 30 | 30 | 30 | **90** |
| **romanticism** | 30 | 30 | 30 | **90** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\linear\2026-07-12\00-50-30_358394\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `linear__impressionism__2026-07-12_00-50-31_319.bin` | 0.05 MB |
| realism | `linear__realism__2026-07-12_00-50-31_319.bin` | 0.05 MB |
| romanticism | `linear__romanticism__2026-07-12_00-50-31_319.bin` | 0.05 MB |

Total size: `0.14 MB`


---

