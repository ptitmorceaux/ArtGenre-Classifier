# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 44.96% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 55.56% | 63.18% | 87.06% | 39.30% | 60.70% | 12.94% |
| realism | 67.06% | 53.47% | 12.58% | 94.36% | 5.64% | 87.42% |
| romanticism | 67.29% | 58.73% | 34.14% | 83.31% | 16.69% | 65.86% |
| **Mean** | **63.30%** | **58.46%** | **44.59%** | **72.32%** | **27.68%** | **55.41%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 3854 | 3371 | 5206 | 573 |
| realism | 546 | 8174 | 489 | 3795 |
| romanticism | 1446 | 7305 | 1463 | 2790 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 40.86% | 54.74% | 98.22% | 11.26% | 88.74% | 1.78% |
| realism | 48.80% | 57.15% | 82.26% | 32.03% | 67.97% | 17.74% |
| romanticism | 35.84% | 51.78% | 97.50% | 6.06% | 93.94% | 2.50% |
| **Mean** | **41.84%** | **54.55%** | **92.66%** | **16.45%** | **83.55%** | **7.34%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 4348 | 966 | 7611 | 79 |
| realism | 3571 | 2775 | 5888 | 770 |
| romanticism | 4130 | 531 | 8237 | 106 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 58.55% |
| realism | 52.50% |
| romanticism | 54.79% |
| **Mean** | **55.28%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `2024` |
| Type | `rbf` |
| Alpha | `0.0001` |
| Epochs | `150` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `29652` |
| Total samples Test | `13004` |
| Limit per category | `9884` |
| Train positive ratio | `0.50` |
| Normalization | `standard` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 9884 | 4427 |
| realism | 9884 | 4341 |
| romanticism | 9884 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 9884 | 4942 | 4942 | **19768** |
| **realism** | 4942 | 9884 | 4942 | **19768** |
| **romanticism** | 4942 | 4942 | 9884 | **19768** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine/core/output/rbf/2026-07-19/23-07-59_194978/confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `rbf__impressionism__2026-07-19_23-09-24_480.bin` | 0.08 MB |
| romanticism | `rbf__romanticism__2026-07-19_23-09-24_480.bin` | 0.08 MB |
| realism | `rbf__realism__2026-07-19_23-09-24_480.bin` | 0.08 MB |

Total size: `0.23 MB`


---

