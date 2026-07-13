# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 37.10% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 62.38% | 55.09% | 32.23% | 77.94% | 22.06% | 67.77% |
| realism | 52.63% | 49.83% | 41.40% | 58.26% | 41.74% | 58.60% |
| romanticism | 59.18% | 53.65% | 37.77% | 69.53% | 30.47% | 62.23% |
| **Mean** | **58.06%** | **52.85%** | **37.13%** | **68.58%** | **31.42%** | **62.87%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1427 | 6685 | 1892 | 3000 |
| realism | 1797 | 5047 | 3616 | 2544 |
| romanticism | 1600 | 6096 | 2672 | 2636 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 59.86% | 55.57% | 42.13% | 69.01% | 30.99% | 57.87% |
| realism | 47.02% | 50.03% | 59.09% | 40.98% | 59.02% | 40.91% |
| romanticism | 58.10% | 53.18% | 39.07% | 67.29% | 32.71% | 60.93% |
| **Mean** | **54.99%** | **52.93%** | **46.76%** | **59.09%** | **40.91%** | **53.24%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1865 | 5919 | 2658 | 2562 |
| realism | 2565 | 3550 | 5113 | 1776 |
| romanticism | 1655 | 5900 | 2868 | 2581 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 68.75% |
| realism | 62.50% |
| romanticism | 68.75% |
| **Mean** | **66.67%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1234` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `10` |
| NPL | `[12288, 10, 10, 1]` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `12` |
| Total samples Test | `13004` |
| Limit per category | `6` |
| Train positive ratio | `0.25` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 4 | 4427 |
| realism | 4 | 4341 |
| romanticism | 4 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 4 | 6 | 6 | **16** |
| **realism** | 6 | 4 | 6 | **16** |
| **romanticism** | 6 | 6 | 4 | **16** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\mlp\2026-07-12\03-06-02_267716\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-12_03-06-02_588.bin` | 0.47 MB |
| realism | `mlp__realism__2026-07-12_03-06-02_588.bin` | 0.47 MB |
| romanticism | `mlp__romanticism__2026-07-12_03-06-02_588.bin` | 0.47 MB |

Total size: `1.41 MB`


---

