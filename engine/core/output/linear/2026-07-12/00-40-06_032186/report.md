# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 42.60% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 63.73% | 56.17% | 32.46% | 79.88% | 20.12% | 67.54% |
| realism | 59.74% | 54.58% | 39.07% | 70.09% | 29.91% | 60.93% |
| romanticism | 61.73% | 60.47% | 56.82% | 64.11% | 35.89% | 43.18% |
| **Mean** | **61.73%** | **57.07%** | **42.78%** | **71.36%** | **28.64%** | **57.22%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1437 | 6851 | 1726 | 2990 |
| realism | 1696 | 6072 | 2591 | 2645 |
| romanticism | 2407 | 5621 | 3147 | 1829 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 63.91% | 54.62% | 25.50% | 83.74% | 16.26% | 74.50% |
| realism | 60.99% | 53.56% | 31.21% | 75.91% | 24.09% | 68.79% |
| romanticism | 63.11% | 59.19% | 47.95% | 70.44% | 29.56% | 52.05% |
| **Mean** | **62.67%** | **55.79%** | **34.89%** | **76.69%** | **23.31%** | **65.11%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1129 | 7182 | 1395 | 3298 |
| realism | 1355 | 6576 | 2087 | 2986 |
| romanticism | 2031 | 6176 | 2592 | 2205 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 82.73% |
| realism | 79.43% |
| romanticism | 80.71% |
| **Mean** | **80.96%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1234` |
| Type | `linear` |
| Alpha | `0.001` |
| Epochs | `100` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `9000` |
| Total samples Test | `13004` |
| Limit per category | `6000` |
| Train positive ratio | `0.20` |
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
| **impressionism** | 3000 | 6000 | 6000 | **15000** |
| **realism** | 6000 | 3000 | 6000 | **15000** |
| **romanticism** | 6000 | 6000 | 3000 | **15000** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\linear\2026-07-12\00-40-06_032186\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `linear__impressionism__2026-07-12_00-41-23_114.bin` | 0.05 MB |
| realism | `linear__realism__2026-07-12_00-41-23_114.bin` | 0.05 MB |
| romanticism | `linear__romanticism__2026-07-12_00-41-23_114.bin` | 0.05 MB |

Total size: `0.14 MB`


---

