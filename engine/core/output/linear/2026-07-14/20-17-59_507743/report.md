# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 46.33% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 65.16% | 61.23% | 48.90% | 73.56% | 26.44% | 51.10% |
| realism | 62.29% | 57.17% | 41.76% | 72.57% | 27.43% | 58.24% |
| romanticism | 65.21% | 60.85% | 48.32% | 73.37% | 26.63% | 51.68% |
| **Mean** | **64.22%** | **59.75%** | **46.33%** | **73.17%** | **26.83%** | **53.67%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2165 | 6309 | 2268 | 2262 |
| realism | 1813 | 6287 | 2376 | 2528 |
| romanticism | 2047 | 6433 | 2335 | 2189 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 63.73% | 56.07% | 32.08% | 80.06% | 19.94% | 67.92% |
| realism | 62.48% | 56.33% | 37.83% | 74.84% | 25.16% | 62.17% |
| romanticism | 65.45% | 60.07% | 44.62% | 75.51% | 24.49% | 55.38% |
| **Mean** | **63.89%** | **57.49%** | **38.17%** | **76.80%** | **23.20%** | **61.83%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1420 | 6867 | 1710 | 3007 |
| realism | 1642 | 6483 | 2180 | 2699 |
| romanticism | 1890 | 6621 | 2147 | 2346 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 74.94% |
| realism | 71.90% |
| romanticism | 73.69% |
| **Mean** | **73.51%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1337` |
| Type | `linear` |
| Alpha | `0.01` |
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
| Confusion Matrix | `engine\core\output\linear\2026-07-14\20-17-59_507743\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `linear__impressionism__2026-07-14_20-22-27_373.bin` | 0.05 MB |
| realism | `linear__realism__2026-07-14_20-22-27_373.bin` | 0.05 MB |
| romanticism | `linear__romanticism__2026-07-14_20-22-27_373.bin` | 0.05 MB |

Total size: `0.14 MB`


---

