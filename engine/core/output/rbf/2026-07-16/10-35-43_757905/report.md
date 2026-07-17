# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 44.46% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 67.43% | 64.37% | 54.75% | 73.98% | 26.02% | 45.25% |
| realism | 61.57% | 57.25% | 44.23% | 70.26% | 29.74% | 55.77% |
| romanticism | 59.90% | 53.19% | 33.92% | 72.46% | 27.54% | 66.08% |
| **Mean** | **62.97%** | **58.27%** | **44.30%** | **72.23%** | **27.77%** | **55.70%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2424 | 6345 | 2232 | 2003 |
| realism | 1920 | 6087 | 2576 | 2421 |
| romanticism | 1437 | 6353 | 2415 | 2799 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 68.29% | 59.09% | 30.25% | 87.93% | 12.07% | 69.75% |
| realism | 66.03% | 53.42% | 15.48% | 91.35% | 8.65% | 84.52% |
| romanticism | 67.06% | 50.26% | 2.03% | 98.48% | 1.52% | 97.97% |
| **Mean** | **67.13%** | **54.25%** | **15.92%** | **92.59%** | **7.41%** | **84.08%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1339 | 7542 | 1035 | 3088 |
| realism | 672 | 7914 | 749 | 3669 |
| romanticism | 86 | 8635 | 133 | 4150 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 67.38% |
| realism | 62.95% |
| romanticism | 64.83% |
| **Mean** | **65.05%** |


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
| Total samples Train (chargées) | `2001` |
| Total samples Test | `13004` |
| Limit per category | `1000` |
| Train positive ratio | `0.25` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 667 | 4427 |
| realism | 667 | 4341 |
| romanticism | 667 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 667 | 1000 | 1000 | **2667** |
| **realism** | 1000 | 667 | 1000 | **2667** |
| **romanticism** | 1000 | 1000 | 667 | **2667** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\rbf\2026-07-16\10-35-43_757905\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `rbf__impressionism__2026-07-16_10-37-29_004.bin` | 0.75 MB |
| realism | `rbf__realism__2026-07-16_10-37-29_004.bin` | 0.75 MB |
| romanticism | `rbf__romanticism__2026-07-16_10-37-29_004.bin` | 0.75 MB |

Total size: `2.25 MB`


---

