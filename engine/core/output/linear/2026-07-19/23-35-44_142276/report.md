# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 38.18% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 61.23% | 52.87% | 26.68% | 79.06% | 20.94% | 73.32% |
| realism | 56.69% | 50.67% | 32.55% | 68.79% | 31.21% | 67.45% |
| romanticism | 58.44% | 57.80% | 55.97% | 59.64% | 40.36% | 44.03% |
| **Mean** | **58.79%** | **53.78%** | **38.40%** | **69.16%** | **30.84%** | **61.60%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1181 | 6781 | 1796 | 3246 |
| realism | 1413 | 5959 | 2704 | 2928 |
| romanticism | 2371 | 5229 | 3539 | 1865 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 61.79% | 50.85% | 16.58% | 85.12% | 14.88% | 83.42% |
| realism | 60.84% | 52.00% | 25.41% | 78.59% | 21.41% | 74.59% |
| romanticism | 65.00% | 56.70% | 32.91% | 80.50% | 19.50% | 67.09% |
| **Mean** | **62.54%** | **53.18%** | **24.97%** | **81.40%** | **18.60%** | **75.03%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 734 | 7301 | 1276 | 3693 |
| realism | 1103 | 6808 | 1855 | 3238 |
| romanticism | 1394 | 7058 | 1710 | 2842 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 64.82% |
| realism | 65.68% |
| romanticism | 66.62% |
| **Mean** | **65.71%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `42` |
| Type | `linear` |
| Alpha | `0.001` |
| Epochs | `75` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `19767` |
| Total samples Test | `13004` |
| Limit per category | `9884` |
| Train positive ratio | `0.25` |
| Normalization | `standard` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 6589 | 4427 |
| realism | 6589 | 4341 |
| romanticism | 6589 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 6589 | 9884 | 9884 | **26357** |
| **realism** | 9884 | 6589 | 9884 | **26357** |
| **romanticism** | 9884 | 9884 | 6589 | **26357** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine/core/output/linear/2026-07-19/23-35-44_142276/confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| romanticism | `linear__romanticism__2026-07-19_23-35-54_573.bin` | 0.00 MB |
| impressionism | `linear__impressionism__2026-07-19_23-35-54_573.bin` | 0.00 MB |
| realism | `linear__realism__2026-07-19_23-35-54_573.bin` | 0.00 MB |

Total size: `0.01 MB`


---

