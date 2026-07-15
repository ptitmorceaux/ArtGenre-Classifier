# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 45.49% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 65.70% | 60.57% | 44.50% | 76.64% | 23.36% | 55.50% |
| realism | 62.02% | 57.66% | 44.55% | 70.77% | 29.23% | 55.45% |
| romanticism | 63.27% | 59.20% | 47.50% | 70.89% | 29.11% | 52.50% |
| **Mean** | **63.66%** | **59.14%** | **45.52%** | **72.77%** | **27.23%** | **54.48%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1970 | 6573 | 2004 | 2457 |
| realism | 1934 | 6131 | 2532 | 2407 |
| romanticism | 2012 | 6216 | 2552 | 2224 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 66.67% | 57.38% | 28.28% | 86.49% | 13.51% | 71.72% |
| realism | 65.36% | 54.37% | 21.29% | 87.45% | 12.55% | 78.71% |
| romanticism | 66.59% | 55.54% | 23.84% | 87.24% | 12.76% | 76.16% |
| **Mean** | **66.21%** | **55.76%** | **24.47%** | **87.06%** | **12.94%** | **75.53%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1252 | 7418 | 1159 | 3175 |
| realism | 924 | 7576 | 1087 | 3417 |
| romanticism | 1010 | 7649 | 1119 | 3226 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 88.42% |
| realism | 83.70% |
| romanticism | 84.99% |
| **Mean** | **85.70%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1234` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `100` |
| NPL | `[12288, 128, 64, 64, 1]` |


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
| Confusion Matrix | `engine\core\output\mlp\2026-07-12\22-30-25_776689\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-13_00-53-58_401.bin` | 6.05 MB |
| realism | `mlp__realism__2026-07-13_00-53-58_401.bin` | 6.05 MB |
| romanticism | `mlp__romanticism__2026-07-13_00-53-58_401.bin` | 6.05 MB |

Total size: `18.14 MB`


---

