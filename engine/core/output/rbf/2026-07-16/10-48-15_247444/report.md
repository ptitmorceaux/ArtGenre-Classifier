# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 36.82% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 66.91% | 55.39% | 19.29% | 91.49% | 8.51% | 80.71% |
| realism | 66.59% | 51.26% | 5.14% | 97.39% | 2.61% | 94.86% |
| romanticism | 40.13% | 52.40% | 87.61% | 17.20% | 82.80% | 12.39% |
| **Mean** | **57.88%** | **53.02%** | **37.34%** | **68.69%** | **31.31%** | **62.66%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 854 | 7847 | 730 | 3573 |
| realism | 223 | 8437 | 226 | 4118 |
| romanticism | 3711 | 1508 | 7260 | 525 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 63.23% | 55.41% | 30.92% | 79.90% | 20.10% | 69.08% |
| realism | 65.30% | 52.70% | 14.77% | 90.63% | 9.37% | 85.23% |
| romanticism | 37.19% | 52.49% | 96.41% | 8.58% | 91.42% | 3.59% |
| **Mean** | **55.24%** | **53.53%** | **47.37%** | **59.70%** | **40.30%** | **52.63%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1369 | 6853 | 1724 | 3058 |
| realism | 641 | 7851 | 812 | 3700 |
| romanticism | 4084 | 752 | 8016 | 152 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 66.09% |
| realism | 63.39% |
| romanticism | 64.17% |
| **Mean** | **64.55%** |


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
| Total samples Train (chargées) | `20229` |
| Total samples Test | `13004` |
| Limit per category | `-1` |
| Train positive ratio | `0.25` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 6671 | 4427 |
| realism | 6738 | 4341 |
| romanticism | 6820 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 6671 | 10130 | 9884 | **26685** |
| **realism** | 10331 | 6738 | 9884 | **26953** |
| **romanticism** | 10331 | 10130 | 6820 | **27281** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\rbf\2026-07-16\10-48-15_247444\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `rbf__impressionism__2026-07-16_11-11-01_563.bin` | 0.75 MB |
| realism | `rbf__realism__2026-07-16_11-11-01_563.bin` | 0.75 MB |
| romanticism | `rbf__romanticism__2026-07-16_11-11-01_563.bin` | 0.75 MB |

Total size: `2.25 MB`


---

