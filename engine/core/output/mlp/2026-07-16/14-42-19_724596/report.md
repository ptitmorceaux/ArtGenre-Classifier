# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 44.92% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 65.37% | 60.78% | 46.40% | 75.17% | 24.83% | 53.60% |
| realism | 61.09% | 56.60% | 43.10% | 70.10% | 29.90% | 56.90% |
| romanticism | 63.37% | 58.68% | 45.23% | 72.14% | 27.86% | 54.77% |
| **Mean** | **63.28%** | **58.69%** | **44.91%** | **72.47%** | **27.53%** | **55.09%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2054 | 6447 | 2130 | 2373 |
| realism | 1871 | 6073 | 2590 | 2470 |
| romanticism | 1916 | 6325 | 2443 | 2320 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 67.06% | 57.11% | 25.93% | 88.29% | 11.71% | 74.07% |
| realism | 65.88% | 54.08% | 18.57% | 89.59% | 10.41% | 81.43% |
| romanticism | 67.15% | 55.40% | 21.67% | 89.12% | 10.88% | 78.33% |
| **Mean** | **66.70%** | **55.53%** | **22.06%** | **89.00%** | **11.00%** | **77.94%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1148 | 7573 | 1004 | 3279 |
| realism | 806 | 7761 | 902 | 3535 |
| romanticism | 918 | 7814 | 954 | 3318 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 83.24% |
| realism | 79.99% |
| romanticism | 80.87% |
| **Mean** | **81.37%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1337` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `40` |
| NPL | `[1024, 64, 16, 1]` |


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
| Confusion Matrix | `engine\core\output\mlp\2026-07-16\14-42-19_724596\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-16_14-45-49_215.bin` | 0.25 MB |
| realism | `mlp__realism__2026-07-16_14-45-49_215.bin` | 0.25 MB |
| romanticism | `mlp__romanticism__2026-07-16_14-45-49_215.bin` | 0.25 MB |

Total size: `0.76 MB`


---

