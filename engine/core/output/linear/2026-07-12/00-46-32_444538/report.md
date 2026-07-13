# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 42.80% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 63.22% | 57.64% | 40.14% | 75.13% | 24.87% | 59.86% |
| realism | 60.12% | 55.49% | 41.56% | 69.42% | 30.58% | 58.44% |
| romanticism | 62.27% | 58.28% | 46.86% | 69.71% | 30.29% | 53.14% |
| **Mean** | **61.87%** | **57.14%** | **42.85%** | **71.42%** | **28.58%** | **57.15%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1777 | 6444 | 2133 | 2650 |
| realism | 1804 | 6014 | 2649 | 2537 |
| romanticism | 1985 | 6112 | 2656 | 2251 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 63.36% | 57.28% | 38.22% | 76.33% | 23.67% | 61.78% |
| realism | 59.23% | 52.40% | 31.86% | 72.94% | 27.06% | 68.14% |
| romanticism | 60.29% | 53.66% | 34.66% | 72.67% | 27.33% | 65.34% |
| **Mean** | **60.96%** | **54.45%** | **34.91%** | **73.98%** | **26.02%** | **65.09%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1692 | 6547 | 2030 | 2735 |
| realism | 1383 | 6319 | 2344 | 2958 |
| romanticism | 1468 | 6372 | 2396 | 2768 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 86.62% |
| realism | 82.50% |
| romanticism | 83.89% |
| **Mean** | **84.34%** |


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
| Total samples Train (chargées) | `6000` |
| Total samples Test | `13004` |
| Limit per category | `3000` |
| Train positive ratio | `0.25` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 2000 | 4427 |
| realism | 2000 | 4341 |
| romanticism | 2000 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 2000 | 3000 | 3000 | **8000** |
| **realism** | 3000 | 2000 | 3000 | **8000** |
| **romanticism** | 3000 | 3000 | 2000 | **8000** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\linear\2026-07-12\00-46-32_444538\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `linear__impressionism__2026-07-12_00-47-04_591.bin` | 0.05 MB |
| realism | `linear__realism__2026-07-12_00-47-04_591.bin` | 0.05 MB |
| romanticism | `linear__romanticism__2026-07-12_00-47-04_591.bin` | 0.05 MB |

Total size: `0.14 MB`


---

