# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 41.61% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 63.25% | 56.79% | 36.55% | 77.03% | 22.97% | 63.45% |
| realism | 59.20% | 53.38% | 35.84% | 70.91% | 29.09% | 64.16% |
| romanticism | 60.77% | 58.71% | 52.81% | 64.61% | 35.39% | 47.19% |
| **Mean** | **61.07%** | **56.29%** | **41.73%** | **70.85%** | **29.15%** | **58.27%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1618 | 6607 | 1970 | 2809 |
| realism | 1556 | 6143 | 2520 | 2785 |
| romanticism | 2237 | 5665 | 3103 | 1999 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 61.15% | 57.13% | 44.54% | 69.72% | 30.28% | 55.46% |
| realism | 56.01% | 53.42% | 45.63% | 61.21% | 38.79% | 54.37% |
| romanticism | 57.20% | 57.17% | 57.11% | 57.24% | 42.76% | 42.89% |
| **Mean** | **58.12%** | **55.91%** | **49.10%** | **62.73%** | **37.27%** | **50.90%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1972 | 5980 | 2597 | 2455 |
| realism | 1981 | 5303 | 3360 | 2360 |
| romanticism | 2419 | 5019 | 3749 | 1817 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 94.80% |
| realism | 93.00% |
| romanticism | 91.87% |
| **Mean** | **93.22%** |


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
| Total samples Train (chargées) | `3000` |
| Total samples Test | `13004` |
| Limit per category | `1000` |
| Train positive ratio | `0.33` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 1000 | 4427 |
| realism | 1000 | 4341 |
| romanticism | 1000 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 1000 | 1000 | 1000 | **3000** |
| **realism** | 1000 | 1000 | 1000 | **3000** |
| **romanticism** | 1000 | 1000 | 1000 | **3000** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\linear\2026-07-11\21-09-02_349430\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `linear__impressionism__2026-07-11_21-09-36_045.bin` | 0.05 MB |
| realism | `linear__realism__2026-07-11_21-09-36_045.bin` | 0.05 MB |
| romanticism | `linear__romanticism__2026-07-11_21-09-36_045.bin` | 0.05 MB |

Total size: `0.14 MB`


---

