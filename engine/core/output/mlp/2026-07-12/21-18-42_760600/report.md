# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 46.72% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 67.23% | 62.32% | 46.94% | 77.71% | 22.29% | 53.06% |
| realism | 62.55% | 57.20% | 41.10% | 73.30% | 26.70% | 58.90% |
| romanticism | 63.65% | 60.70% | 52.24% | 69.16% | 30.84% | 47.76% |
| **Mean** | **64.48%** | **60.07%** | **46.76%** | **73.39%** | **26.61%** | **53.24%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2078 | 6665 | 1912 | 2349 |
| realism | 1784 | 6350 | 2313 | 2557 |
| romanticism | 2213 | 6064 | 2704 | 2023 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 68.59% | 58.81% | 28.15% | 89.47% | 10.53% | 71.85% |
| realism | 66.24% | 54.76% | 20.23% | 89.30% | 10.70% | 79.77% |
| romanticism | 68.23% | 57.56% | 26.94% | 88.18% | 11.82% | 73.06% |
| **Mean** | **67.69%** | **57.04%** | **25.10%** | **88.99%** | **11.01%** | **74.90%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1246 | 7674 | 903 | 3181 |
| realism | 878 | 7736 | 927 | 3463 |
| romanticism | 1141 | 7732 | 1036 | 3095 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 84.97% |
| realism | 80.91% |
| romanticism | 84.00% |
| **Mean** | **83.29%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `2024` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `100` |
| NPL | `[12288, 256, 256, 1]` |


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
| Confusion Matrix | `engine\core\output\mlp\2026-07-12\21-18-42_760600\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-13_06-04-30_986.bin` | 12.25 MB |
| realism | `mlp__realism__2026-07-13_06-04-30_986.bin` | 12.25 MB |
| romanticism | `mlp__romanticism__2026-07-13_06-04-30_986.bin` | 12.25 MB |

Total size: `36.76 MB`


---

