# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 45.82% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 66.57% | 59.83% | 38.69% | 80.96% | 19.04% | 61.31% |
| realism | 60.80% | 57.66% | 48.21% | 67.10% | 32.90% | 51.79% |
| romanticism | 64.28% | 60.80% | 50.83% | 70.78% | 29.22% | 49.17% |
| **Mean** | **63.88%** | **59.43%** | **45.91%** | **72.95%** | **27.05%** | **54.09%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1713 | 6944 | 1633 | 2714 |
| realism | 2093 | 5813 | 2850 | 2248 |
| romanticism | 2153 | 6206 | 2562 | 2083 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 67.64% | 56.92% | 23.31% | 90.52% | 9.48% | 76.69% |
| realism | 66.28% | 55.99% | 25.04% | 86.94% | 13.06% | 74.96% |
| romanticism | 68.69% | 59.03% | 31.33% | 86.74% | 13.26% | 68.67% |
| **Mean** | **67.54%** | **57.31%** | **26.56%** | **88.07%** | **11.93%** | **73.44%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1032 | 7764 | 813 | 3395 |
| realism | 1087 | 7532 | 1131 | 3254 |
| romanticism | 1327 | 7605 | 1163 | 2909 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 87.74% |
| realism | 88.48% |
| romanticism | 90.12% |
| **Mean** | **88.78%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1337` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `40` |
| NPL | `[1024, 256, 128, 1]` |


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
| Confusion Matrix | `engine\core\output\mlp\2026-07-16\13-18-37_217181\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-16_13-45-39_483.bin` | 1.13 MB |
| realism | `mlp__realism__2026-07-16_13-45-39_483.bin` | 1.13 MB |
| romanticism | `mlp__romanticism__2026-07-16_13-45-39_483.bin` | 1.13 MB |

Total size: `3.38 MB`


---

