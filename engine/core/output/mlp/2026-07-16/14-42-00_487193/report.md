# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 44.63% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 64.41% | 59.18% | 42.78% | 75.57% | 24.43% | 57.22% |
| realism | 61.07% | 57.15% | 45.34% | 68.96% | 31.04% | 54.66% |
| romanticism | 63.78% | 59.15% | 45.85% | 72.45% | 27.55% | 54.15% |
| **Mean** | **63.09%** | **58.49%** | **44.65%** | **72.33%** | **27.67%** | **55.35%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1894 | 6482 | 2095 | 2533 |
| realism | 1968 | 5974 | 2689 | 2373 |
| romanticism | 1942 | 6352 | 2416 | 2294 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 66.04% | 57.21% | 29.55% | 84.88% | 15.12% | 70.45% |
| realism | 64.33% | 54.72% | 25.80% | 83.63% | 16.37% | 74.20% |
| romanticism | 66.87% | 57.80% | 31.75% | 83.84% | 16.16% | 68.25% |
| **Mean** | **65.75%** | **56.57%** | **29.03%** | **84.12%** | **15.88%** | **70.97%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1308 | 7280 | 1297 | 3119 |
| realism | 1120 | 7245 | 1418 | 3221 |
| romanticism | 1345 | 7351 | 1417 | 2891 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 90.15% |
| realism | 87.31% |
| romanticism | 88.67% |
| **Mean** | **88.71%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1337` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `40` |
| NPL | `[1024, 128, 32, 1]` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `20229` |
| Total samples Test | `13004` |
| Limit per category | `-1` |
| Train positive ratio | `0.25` |
| Normalization | `standard` |

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
| Confusion Matrix | `engine\core\output\mlp\2026-07-16\14-42-00_487193\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-16_14-54-55_573.bin` | 0.52 MB |
| realism | `mlp__realism__2026-07-16_14-54-55_573.bin` | 0.52 MB |
| romanticism | `mlp__romanticism__2026-07-16_14-54-55_573.bin` | 0.52 MB |

Total size: `1.55 MB`


---

