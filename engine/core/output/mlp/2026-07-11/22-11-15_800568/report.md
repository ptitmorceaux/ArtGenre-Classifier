# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 43.95% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 64.73% | 59.69% | 43.87% | 75.50% | 24.50% | 56.13% |
| realism | 60.57% | 55.44% | 40.01% | 70.88% | 29.12% | 59.99% |
| romanticism | 62.59% | 58.83% | 48.06% | 69.61% | 30.39% | 51.94% |
| **Mean** | **62.63%** | **57.99%** | **43.98%** | **72.00%** | **28.00%** | **56.02%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1942 | 6476 | 2101 | 2485 |
| realism | 1737 | 6140 | 2523 | 2604 |
| romanticism | 2036 | 6103 | 2665 | 2200 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 64.06% | 58.29% | 40.21% | 76.38% | 23.62% | 59.79% |
| realism | 60.42% | 54.40% | 36.28% | 72.52% | 27.48% | 63.72% |
| romanticism | 63.03% | 58.35% | 44.92% | 71.78% | 28.22% | 55.08% |
| **Mean** | **62.51%** | **57.02%** | **40.47%** | **73.56%** | **26.44%** | **59.53%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1780 | 6551 | 2026 | 2647 |
| realism | 1575 | 6282 | 2381 | 2766 |
| romanticism | 1903 | 6294 | 2474 | 2333 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 93.78% |
| realism | 90.20% |
| romanticism | 91.42% |
| **Mean** | **91.80%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `2024` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `100` |
| NPL | `[12288, 64, 64, 1]` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `9000` |
| Total samples Test | `13004` |
| Limit per category | `3000` |
| Train positive ratio | `0.33` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 3000 | 4427 |
| realism | 3000 | 4341 |
| romanticism | 3000 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 3000 | 3000 | 3000 | **9000** |
| **realism** | 3000 | 3000 | 3000 | **9000** |
| **romanticism** | 3000 | 3000 | 3000 | **9000** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\mlp\2026-07-11\22-11-15_800568\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-11_22-36-52_374.bin` | 3.02 MB |
| realism | `mlp__realism__2026-07-11_22-36-52_374.bin` | 3.02 MB |
| romanticism | `mlp__romanticism__2026-07-11_22-36-52_374.bin` | 3.02 MB |

Total size: `9.05 MB`


---

