# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 46.55% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 67.75% | 62.42% | 45.72% | 79.12% | 20.88% | 54.28% |
| realism | 60.48% | 56.47% | 44.39% | 68.54% | 31.46% | 55.61% |
| romanticism | 64.86% | 60.93% | 49.62% | 72.23% | 27.77% | 50.38% |
| **Mean** | **64.36%** | **59.94%** | **46.58%** | **73.30%** | **26.70%** | **53.42%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2024 | 6786 | 1791 | 2403 |
| realism | 1927 | 5938 | 2725 | 2414 |
| romanticism | 2102 | 6333 | 2435 | 2134 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 68.06% | 58.38% | 28.06% | 88.70% | 11.30% | 71.94% |
| realism | 64.96% | 53.93% | 20.76% | 87.11% | 12.89% | 79.24% |
| romanticism | 67.80% | 57.52% | 28.02% | 87.02% | 12.98% | 71.98% |
| **Mean** | **66.94%** | **56.61%** | **25.61%** | **87.61%** | **12.39%** | **74.39%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1242 | 7608 | 969 | 3185 |
| realism | 901 | 7546 | 1117 | 3440 |
| romanticism | 1187 | 7630 | 1138 | 3049 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 87.84% |
| realism | 82.79% |
| romanticism | 82.68% |
| **Mean** | **84.44%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1234` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `100` |
| NPL | `[12288, 128, 128, 128, 1]` |


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
| Confusion Matrix | `engine\core\output\mlp\2026-07-13\12-27-09_725625\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-13_16-28-57_437.bin` | 6.13 MB |
| realism | `mlp__realism__2026-07-13_16-28-57_437.bin` | 6.13 MB |
| romanticism | `mlp__romanticism__2026-07-13_16-28-57_437.bin` | 6.13 MB |

Total size: `18.38 MB`


---

