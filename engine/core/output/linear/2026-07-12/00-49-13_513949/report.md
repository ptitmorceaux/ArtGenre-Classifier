# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 36.80% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 60.10% | 53.25% | 31.78% | 74.72% | 25.28% | 68.22% |
| realism | 55.78% | 51.77% | 39.69% | 63.85% | 36.15% | 60.31% |
| romanticism | 57.72% | 52.91% | 39.09% | 66.72% | 33.28% | 60.91% |
| **Mean** | **57.87%** | **52.64%** | **36.86%** | **68.43%** | **31.57%** | **63.14%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1407 | 6409 | 2168 | 3020 |
| realism | 1723 | 5531 | 3132 | 2618 |
| romanticism | 1656 | 5850 | 2918 | 2580 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 57.31% | 54.05% | 43.82% | 64.28% | 35.72% | 56.18% |
| realism | 52.45% | 51.83% | 49.94% | 53.71% | 46.29% | 50.06% |
| romanticism | 52.70% | 51.42% | 47.73% | 55.10% | 44.90% | 52.27% |
| **Mean** | **54.16%** | **52.43%** | **47.17%** | **57.70%** | **42.30%** | **52.83%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1940 | 5513 | 3064 | 2487 |
| realism | 2168 | 4653 | 4010 | 2173 |
| romanticism | 2022 | 4831 | 3937 | 2214 |


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
| Train positive ratio | `désactivé (-1)` |
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
| Confusion Matrix | `engine\core\output\linear\2026-07-12\00-49-13_513949\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `linear__impressionism__2026-07-12_00-49-15_804.bin` | 0.05 MB |
| realism | `linear__realism__2026-07-12_00-49-15_804.bin` | 0.05 MB |
| romanticism | `linear__romanticism__2026-07-12_00-49-15_804.bin` | 0.05 MB |

Total size: `0.14 MB`


---

