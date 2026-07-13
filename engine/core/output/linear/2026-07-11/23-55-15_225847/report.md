# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 41.34% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 66.10% | 58.13% | 33.18% | 83.08% | 16.92% | 66.82% |
| realism | 57.27% | 55.48% | 50.08% | 60.88% | 39.12% | 49.92% |
| romanticism | 59.31% | 54.56% | 40.91% | 68.20% | 31.80% | 59.09% |
| **Mean** | **60.89%** | **56.06%** | **41.39%** | **70.72%** | **29.28%** | **58.61%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1469 | 7126 | 1451 | 2958 |
| realism | 2174 | 5274 | 3389 | 2167 |
| romanticism | 1733 | 5980 | 2788 | 2503 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 60.80% | 58.28% | 50.37% | 66.19% | 33.81% | 49.63% |
| realism | 53.87% | 55.31% | 59.64% | 50.98% | 49.02% | 40.36% |
| romanticism | 54.75% | 54.21% | 52.67% | 55.76% | 44.24% | 47.33% |
| **Mean** | **56.47%** | **55.93%** | **54.23%** | **57.64%** | **42.36%** | **45.77%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2230 | 5677 | 2900 | 2197 |
| realism | 2589 | 4416 | 4247 | 1752 |
| romanticism | 2231 | 4889 | 3879 | 2005 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 73.46% |
| realism | 70.65% |
| romanticism | 72.19% |
| **Mean** | **72.10%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1234` |
| Type | `linear` |
| Alpha | `0.001` |
| Epochs | `100` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `18000` |
| Total samples Test | `13004` |
| Limit per category | `6000` |
| Train positive ratio | `0.50` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 6000 | 4427 |
| realism | 6000 | 4341 |
| romanticism | 6000 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 6000 | 3000 | 3000 | **12000** |
| **realism** | 3000 | 6000 | 3000 | **12000** |
| **romanticism** | 3000 | 3000 | 6000 | **12000** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\linear\2026-07-11\23-55-15_225847\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `linear__impressionism__2026-07-11_23-56-46_118.bin` | 0.05 MB |
| realism | `linear__realism__2026-07-11_23-56-46_118.bin` | 0.05 MB |
| romanticism | `linear__romanticism__2026-07-11_23-56-46_118.bin` | 0.05 MB |

Total size: `0.14 MB`


---

