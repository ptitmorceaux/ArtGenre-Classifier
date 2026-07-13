# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 39.58% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 60.68% | 56.27% | 42.47% | 70.08% | 29.92% | 57.53% |
| realism | 58.23% | 52.87% | 36.77% | 68.98% | 31.02% | 63.23% |
| romanticism | 60.25% | 54.87% | 39.45% | 70.30% | 29.70% | 60.55% |
| **Mean** | **59.72%** | **54.67%** | **39.56%** | **69.79%** | **30.21%** | **60.44%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1880 | 6011 | 2566 | 2547 |
| realism | 1596 | 5976 | 2687 | 2745 |
| romanticism | 1671 | 6164 | 2604 | 2565 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 57.07% | 56.88% | 56.31% | 57.46% | 42.54% | 43.69% |
| realism | 52.82% | 52.75% | 52.55% | 52.96% | 47.04% | 47.45% |
| romanticism | 52.23% | 53.44% | 56.89% | 49.98% | 50.02% | 43.11% |
| **Mean** | **54.04%** | **54.36%** | **55.25%** | **53.46%** | **46.54%** | **44.75%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2493 | 4928 | 3649 | 1934 |
| realism | 2281 | 4588 | 4075 | 2060 |
| romanticism | 2410 | 4382 | 4386 | 1826 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 83.15% |
| realism | 76.90% |
| romanticism | 77.05% |
| **Mean** | **79.03%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `5678` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `100` |
| NPL | `[12288, 16, 16, 1]` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `3000` |
| Total samples Test | `13004` |
| Limit per category | `1000` |
| Train positive ratio | `0.50` |
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
| **impressionism** | 1000 | 500 | 500 | **2000** |
| **realism** | 500 | 1000 | 500 | **2000** |
| **romanticism** | 500 | 500 | 1000 | **2000** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\mlp\2026-07-11\21-30-14_564265\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-11_21-31-56_186.bin` | 0.75 MB |
| realism | `mlp__realism__2026-07-11_21-31-56_186.bin` | 0.75 MB |
| romanticism | `mlp__romanticism__2026-07-11_21-31-56_186.bin` | 0.75 MB |

Total size: `2.25 MB`


---

