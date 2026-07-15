# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 45.29% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 65.63% | 61.17% | 47.17% | 75.17% | 24.83% | 52.83% |
| realism | 61.48% | 57.13% | 44.02% | 70.23% | 29.77% | 55.98% |
| romanticism | 63.46% | 58.59% | 44.62% | 72.56% | 27.44% | 55.38% |
| **Mean** | **63.52%** | **58.96%** | **45.27%** | **72.65%** | **27.35%** | **54.73%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2088 | 6447 | 2130 | 2339 |
| realism | 1911 | 6084 | 2579 | 2430 |
| romanticism | 1890 | 6362 | 2406 | 2346 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 67.28% | 58.60% | 31.42% | 85.79% | 14.21% | 68.58% |
| realism | 64.72% | 54.73% | 24.67% | 84.79% | 15.21% | 75.33% |
| romanticism | 67.13% | 57.11% | 28.35% | 85.87% | 14.13% | 71.65% |
| **Mean** | **66.38%** | **56.81%** | **28.15%** | **85.48%** | **14.52%** | **71.85%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1391 | 7358 | 1219 | 3036 |
| realism | 1071 | 7345 | 1318 | 3270 |
| romanticism | 1201 | 7529 | 1239 | 3035 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 89.39% |
| realism | 83.07% |
| romanticism | 85.75% |
| **Mean** | **86.07%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `5678` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `100` |
| NPL | `[12288, 64, 64, 64, 1]` |


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
| Confusion Matrix | `engine\core\output\mlp\2026-07-12\20-50-23_426125\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-12_21-40-59_831.bin` | 3.03 MB |
| realism | `mlp__realism__2026-07-12_21-40-59_831.bin` | 3.03 MB |
| romanticism | `mlp__romanticism__2026-07-12_21-40-59_831.bin` | 3.03 MB |

Total size: `9.10 MB`


---

