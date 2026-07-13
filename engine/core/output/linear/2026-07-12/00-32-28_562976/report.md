# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 44.99% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 64.50% | 59.95% | 45.72% | 74.19% | 25.81% | 54.28% |
| realism | 62.07% | 55.70% | 36.56% | 74.85% | 25.15% | 63.44% |
| romanticism | 63.41% | 60.68% | 52.86% | 68.51% | 31.49% | 47.14% |
| **Mean** | **63.32%** | **58.78%** | **45.04%** | **72.51%** | **27.49%** | **54.96%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2024 | 6363 | 2214 | 2403 |
| realism | 1587 | 6484 | 2179 | 2754 |
| romanticism | 2239 | 6007 | 2761 | 1997 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 62.69% | 57.74% | 42.24% | 73.24% | 26.76% | 57.76% |
| realism | 62.61% | 56.12% | 36.60% | 75.64% | 24.36% | 63.40% |
| romanticism | 63.26% | 59.67% | 49.39% | 69.96% | 30.04% | 50.61% |
| **Mean** | **62.85%** | **57.85%** | **42.74%** | **72.95%** | **27.05%** | **57.26%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1870 | 6282 | 2295 | 2557 |
| realism | 1589 | 6553 | 2110 | 2752 |
| romanticism | 2092 | 6134 | 2634 | 2144 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 78.49% |
| realism | 76.04% |
| romanticism | 77.36% |
| **Mean** | **77.30%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `2024` |
| Type | `linear` |
| Alpha | `0.001` |
| Epochs | `100` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `12000` |
| Total samples Test | `13004` |
| Limit per category | `6000` |
| Train positive ratio | `0.25` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 4000 | 4427 |
| realism | 4000 | 4341 |
| romanticism | 4000 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 4000 | 6000 | 6000 | **16000** |
| **realism** | 6000 | 4000 | 6000 | **16000** |
| **romanticism** | 6000 | 6000 | 4000 | **16000** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\linear\2026-07-12\00-32-28_562976\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `linear__impressionism__2026-07-12_00-33-47_940.bin` | 0.05 MB |
| realism | `linear__realism__2026-07-12_00-33-47_940.bin` | 0.05 MB |
| romanticism | `linear__romanticism__2026-07-12_00-33-47_940.bin` | 0.05 MB |

Total size: `0.14 MB`


---

