# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 43.56% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 69.12% | 64.32% | 49.29% | 79.35% | 20.65% | 50.71% |
| realism | 65.85% | 50.40% | 3.92% | 96.88% | 3.12% | 96.08% |
| romanticism | 52.16% | 58.89% | 78.21% | 39.58% | 60.42% | 21.79% |
| **Mean** | **62.38%** | **57.87%** | **43.81%** | **71.94%** | **28.06%** | **56.19%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2182 | 6806 | 1771 | 2245 |
| realism | 170 | 8393 | 270 | 4171 |
| romanticism | 3313 | 3470 | 5298 | 923 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 67.37% | 53.39% | 9.58% | 97.20% | 2.80% | 90.42% |
| realism | 66.62% | 50.00% | 0.00% | 100.00% | 0.00% | 100.00% |
| romanticism | 63.75% | 56.11% | 34.21% | 78.02% | 21.98% | 65.79% |
| **Mean** | **65.91%** | **53.17%** | **14.59%** | **91.74%** | **8.26%** | **85.41%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 424 | 8337 | 240 | 4003 |
| realism | 0 | 8663 | 0 | 4341 |
| romanticism | 1449 | 6841 | 1927 | 2787 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 61.87% |
| realism | 58.13% |
| romanticism | 58.07% |
| **Mean** | **59.36%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `42` |
| Type | `rbf` |
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
| Train positive ratio | `désactivé (-1)` |
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
| Confusion Matrix | `engine\core\output\rbf\2026-07-16\10-01-25_981741\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `rbf__impressionism__2026-07-16_10-02-11_535.bin` | 0.38 MB |
| realism | `rbf__realism__2026-07-16_10-02-11_535.bin` | 0.38 MB |
| romanticism | `rbf__romanticism__2026-07-16_10-02-11_535.bin` | 0.38 MB |

Total size: `1.13 MB`


---

