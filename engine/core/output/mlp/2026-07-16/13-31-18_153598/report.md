# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 46.62% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 66.64% | 61.81% | 46.67% | 76.95% | 23.05% | 53.33% |
| realism | 62.11% | 57.46% | 43.47% | 71.45% | 28.55% | 56.53% |
| romanticism | 64.48% | 60.68% | 49.79% | 71.58% | 28.42% | 50.21% |
| **Mean** | **64.41%** | **59.98%** | **46.64%** | **73.33%** | **26.67%** | **53.36%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2066 | 6600 | 1977 | 2361 |
| realism | 1887 | 6190 | 2473 | 2454 |
| romanticism | 2109 | 6276 | 2492 | 2127 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 68.46% | 57.71% | 24.03% | 91.38% | 8.62% | 75.97% |
| realism | 66.77% | 54.82% | 18.84% | 90.79% | 9.21% | 81.16% |
| romanticism | 69.69% | 58.53% | 26.53% | 90.53% | 9.47% | 73.47% |
| **Mean** | **68.30%** | **57.02%** | **23.14%** | **90.90%** | **9.10%** | **76.86%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1064 | 7838 | 739 | 3363 |
| realism | 818 | 7865 | 798 | 3523 |
| romanticism | 1124 | 7938 | 830 | 3112 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 84.90% |
| realism | 82.48% |
| romanticism | 84.69% |
| **Mean** | **84.02%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1337` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `40` |
| NPL | `[1024, 256, 256, 1]` |


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
| Confusion Matrix | `engine\core\output\mlp\2026-07-16\13-31-18_153598\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-16_13-51-18_055.bin` | 1.25 MB |
| realism | `mlp__realism__2026-07-16_13-51-18_055.bin` | 1.25 MB |
| romanticism | `mlp__romanticism__2026-07-16_13-51-18_055.bin` | 1.25 MB |

Total size: `3.76 MB`


---

