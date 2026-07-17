# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 47.12% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 67.46% | 61.11% | 41.22% | 81.00% | 19.00% | 58.78% |
| realism | 61.58% | 58.25% | 48.24% | 68.27% | 31.73% | 51.76% |
| romanticism | 65.20% | 61.82% | 52.12% | 71.51% | 28.49% | 47.88% |
| **Mean** | **64.74%** | **60.39%** | **47.20%** | **73.59%** | **26.41%** | **52.80%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1825 | 6947 | 1630 | 2602 |
| realism | 2094 | 5914 | 2749 | 2247 |
| romanticism | 2208 | 6270 | 2498 | 2028 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 68.74% | 58.39% | 25.98% | 90.81% | 9.19% | 74.02% |
| realism | 66.39% | 56.15% | 25.32% | 86.98% | 13.02% | 74.68% |
| romanticism | 69.72% | 60.17% | 32.77% | 87.58% | 12.42% | 67.23% |
| **Mean** | **68.29%** | **58.24%** | **28.02%** | **88.46%** | **11.54%** | **71.98%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1150 | 7789 | 788 | 3277 |
| realism | 1099 | 7535 | 1128 | 3242 |
| romanticism | 1388 | 7679 | 1089 | 2848 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 88.98% |
| realism | 90.74% |
| romanticism | 91.80% |
| **Mean** | **90.51%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1337` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `100` |
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
| Confusion Matrix | `engine\core\output\mlp\2026-07-16\13-32-20_591219\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-16_14-28-24_067.bin` | 1.25 MB |
| realism | `mlp__realism__2026-07-16_14-28-24_067.bin` | 1.25 MB |
| romanticism | `mlp__romanticism__2026-07-16_14-28-24_067.bin` | 1.25 MB |

Total size: `3.76 MB`


---

