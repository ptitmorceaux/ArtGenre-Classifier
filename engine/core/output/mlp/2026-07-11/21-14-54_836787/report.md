# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 40.43% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 61.82% | 57.30% | 43.12% | 71.47% | 28.53% | 56.88% |
| realism | 59.00% | 52.70% | 33.72% | 71.67% | 28.33% | 66.28% |
| romanticism | 60.04% | 56.03% | 44.50% | 67.55% | 32.45% | 55.50% |
| **Mean** | **60.29%** | **55.34%** | **40.45%** | **70.23%** | **29.77%** | **59.55%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1909 | 6130 | 2447 | 2518 |
| realism | 1464 | 6209 | 2454 | 2877 |
| romanticism | 1885 | 5923 | 2845 | 2351 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 63.33% | 56.48% | 35.04% | 77.93% | 22.07% | 64.96% |
| realism | 60.44% | 51.93% | 26.31% | 77.55% | 22.45% | 73.69% |
| romanticism | 60.57% | 53.64% | 33.78% | 73.51% | 26.49% | 66.22% |
| **Mean** | **61.45%** | **54.02%** | **31.71%** | **76.33%** | **23.67%** | **68.29%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1551 | 6684 | 1893 | 2876 |
| realism | 1142 | 6718 | 1945 | 3199 |
| romanticism | 1431 | 6445 | 2323 | 2805 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 79.10% |
| realism | 78.27% |
| romanticism | 79.27% |
| **Mean** | **78.88%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `2024` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `100` |
| NPL | `[12288, 16, 16, 1]` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `3000` |
| Total samples Test | `13004` |
| Limit per category | `1000` |
| Train positive ratio | `0.33` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 1000 | 4427 |
| realism | 1000 | 4341 |
| romanticism | 1000 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 1000 | 1000 | 1000 | **3000** |
| **realism** | 1000 | 1000 | 1000 | **3000** |
| **romanticism** | 1000 | 1000 | 1000 | **3000** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\mlp\2026-07-11\21-14-54_836787\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-11_21-21-08_894.bin` | 0.75 MB |
| realism | `mlp__realism__2026-07-11_21-21-08_894.bin` | 0.75 MB |
| romanticism | `mlp__romanticism__2026-07-11_21-21-08_894.bin` | 0.75 MB |

Total size: `2.25 MB`


---

