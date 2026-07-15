# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 43.11% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 66.17% | 60.46% | 42.56% | 78.36% | 21.64% | 57.44% |
| realism | 58.78% | 53.62% | 38.08% | 69.16% | 30.84% | 61.92% |
| romanticism | 61.27% | 58.06% | 48.84% | 67.27% | 32.73% | 51.16% |
| **Mean** | **62.07%** | **57.38%** | **43.16%** | **71.59%** | **28.41%** | **56.84%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1884 | 6721 | 1856 | 2543 |
| realism | 1653 | 5991 | 2672 | 2688 |
| romanticism | 2069 | 5898 | 2870 | 2167 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 67.73% | 56.94% | 23.13% | 90.75% | 9.25% | 76.87% |
| realism | 64.17% | 52.12% | 15.85% | 88.39% | 11.61% | 84.15% |
| romanticism | 66.09% | 53.50% | 17.37% | 89.62% | 10.38% | 82.63% |
| **Mean** | **66.00%** | **54.19%** | **18.78%** | **89.59%** | **10.41%** | **81.22%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1024 | 7784 | 793 | 3403 |
| realism | 688 | 7657 | 1006 | 3653 |
| romanticism | 736 | 7858 | 910 | 3500 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 85.04% |
| realism | 80.35% |
| romanticism | 81.40% |
| **Mean** | **82.26%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `2024` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `100` |
| NPL | `[12288, 128, 128, 128, 1]` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `3999` |
| Total samples Test | `13004` |
| Limit per category | `2000` |
| Train positive ratio | `0.25` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 1333 | 4427 |
| realism | 1333 | 4341 |
| romanticism | 1333 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 1333 | 2000 | 2000 | **5333** |
| **realism** | 2000 | 1333 | 2000 | **5333** |
| **romanticism** | 2000 | 2000 | 1333 | **5333** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine/core/output/mlp/2026-07-13/18-03-59_211388/confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| realism | `mlp__realism__2026-07-13_18-56-33_865.bin` | 6.13 MB |
| impressionism | `mlp__impressionism__2026-07-13_18-56-33_865.bin` | 6.13 MB |
| romanticism | `mlp__romanticism__2026-07-13_18-56-33_865.bin` | 6.13 MB |

Total size: `18.38 MB`


---

