# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 46.62% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 67.20% | 63.15% | 50.46% | 75.84% | 24.16% | 49.54% |
| realism | 63.64% | 56.07% | 33.29% | 78.85% | 21.15% | 66.71% |
| romanticism | 62.40% | 60.82% | 56.28% | 65.36% | 34.64% | 43.72% |
| **Mean** | **64.42%** | **60.01%** | **46.68%** | **73.35%** | **26.65%** | **53.32%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2234 | 6505 | 2072 | 2193 |
| realism | 1445 | 6831 | 1832 | 2896 |
| romanticism | 2384 | 5731 | 3037 | 1852 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 68.82% | 57.03% | 20.06% | 94.00% | 6.00% | 79.94% |
| realism | 66.47% | 52.65% | 11.08% | 94.23% | 5.77% | 88.92% |
| romanticism | 68.76% | 55.83% | 18.72% | 92.94% | 7.06% | 81.28% |
| **Mean** | **68.02%** | **55.17%** | **16.62%** | **93.72%** | **6.28%** | **83.38%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 888 | 8062 | 515 | 3539 |
| realism | 481 | 8163 | 500 | 3860 |
| romanticism | 793 | 8149 | 619 | 3443 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 80.28% |
| realism | 77.13% |
| romanticism | 78.10% |
| **Mean** | **78.50%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1337` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `40` |
| NPL | `[12288, 256, 256, 1]` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `20229` |
| Total samples Test | `13004` |
| Limit per category | `-1` |
| Train positive ratio | `0.25` |
| Normalization | `per_column` |

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
| Confusion Matrix | `engine\core\output\mlp\2026-07-16\11-46-29_772800\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-16_19-34-50_262.bin` | 12.25 MB |
| realism | `mlp__realism__2026-07-16_19-34-50_262.bin` | 12.25 MB |
| romanticism | `mlp__romanticism__2026-07-16_19-34-50_262.bin` | 12.25 MB |

Total size: `36.76 MB`


---

