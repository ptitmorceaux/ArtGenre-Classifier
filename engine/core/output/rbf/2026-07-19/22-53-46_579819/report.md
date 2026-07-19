# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 44.50% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 54.64% | 62.92% | 88.86% | 36.98% | 63.02% | 11.14% |
| realism | 67.19% | 52.03% | 6.43% | 97.63% | 2.37% | 93.57% |
| romanticism | 67.17% | 59.41% | 37.16% | 81.67% | 18.33% | 62.84% |
| **Mean** | **63.00%** | **58.12%** | **44.15%** | **72.10%** | **27.90%** | **55.85%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 3934 | 3172 | 5405 | 493 |
| realism | 279 | 8458 | 205 | 4062 |
| romanticism | 1574 | 7161 | 1607 | 2662 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 40.79% | 54.76% | 98.53% | 10.98% | 89.02% | 1.47% |
| realism | 52.00% | 57.54% | 74.20% | 40.87% | 59.13% | 25.80% |
| romanticism | 35.08% | 51.23% | 97.57% | 4.89% | 95.11% | 2.43% |
| **Mean** | **42.62%** | **54.51%** | **90.10%** | **18.92%** | **81.08%** | **9.90%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 4362 | 942 | 7635 | 65 |
| realism | 3221 | 3541 | 5122 | 1120 |
| romanticism | 4133 | 429 | 8339 | 103 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 58.38% |
| realism | 52.22% |
| romanticism | 54.70% |
| **Mean** | **55.10%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `2024` |
| Type | `rbf` |
| Alpha | `0.0001` |
| Epochs | `200` |


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
| Confusion Matrix | `engine/core/output/rbf/2026-07-19/22-53-46_579819/confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `rbf__impressionism__2026-07-19_22-55-12_524.bin` | 0.08 MB |
| realism | `rbf__realism__2026-07-19_22-55-12_524.bin` | 0.08 MB |
| romanticism | `rbf__romanticism__2026-07-19_22-55-12_524.bin` | 0.08 MB |

Total size: `0.23 MB`


---

