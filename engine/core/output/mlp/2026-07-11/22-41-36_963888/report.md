# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 45.39% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 66.36% | 60.79% | 43.33% | 78.26% | 21.74% | 56.67% |
| realism | 61.14% | 57.10% | 44.94% | 69.25% | 30.75% | 55.06% |
| romanticism | 63.27% | 59.32% | 47.99% | 70.65% | 29.35% | 52.01% |
| **Mean** | **63.59%** | **59.07%** | **45.42%** | **72.72%** | **27.28%** | **54.58%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1918 | 6712 | 1865 | 2509 |
| realism | 1951 | 5999 | 2664 | 2390 |
| romanticism | 2033 | 6195 | 2573 | 2203 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 66.42% | 60.36% | 41.38% | 79.34% | 20.66% | 58.62% |
| realism | 61.17% | 55.63% | 38.95% | 72.30% | 27.70% | 61.05% |
| romanticism | 63.33% | 58.03% | 42.85% | 73.22% | 26.78% | 57.15% |
| **Mean** | **63.64%** | **58.01%** | **41.06%** | **74.95%** | **25.05%** | **58.94%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1832 | 6805 | 1772 | 2595 |
| realism | 1691 | 6263 | 2400 | 2650 |
| romanticism | 1815 | 6420 | 2348 | 2421 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 94.16% |
| realism | 91.41% |
| romanticism | 91.44% |
| **Mean** | **92.34%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `42` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `100` |
| NPL | `[12288, 128, 128, 1]` |


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
| Confusion Matrix | `engine\core\output\mlp\2026-07-11\22-41-36_963888\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-11_23-34-38_248.bin` | 6.06 MB |
| realism | `mlp__realism__2026-07-11_23-34-38_248.bin` | 6.06 MB |
| romanticism | `mlp__romanticism__2026-07-11_23-34-38_248.bin` | 6.06 MB |

Total size: `18.19 MB`


---

