# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 45.72% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 67.09% | 61.72% | 44.91% | 78.54% | 21.46% | 55.09% |
| realism | 60.75% | 56.88% | 45.22% | 68.53% | 31.47% | 54.78% |
| romanticism | 63.60% | 59.33% | 47.07% | 71.58% | 28.42% | 52.93% |
| **Mean** | **63.81%** | **59.31%** | **45.73%** | **72.88%** | **27.12%** | **54.27%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1988 | 6736 | 1841 | 2439 |
| realism | 1963 | 5937 | 2726 | 2378 |
| romanticism | 1994 | 6276 | 2492 | 2242 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 67.58% | 58.52% | 30.13% | 86.91% | 13.09% | 69.87% |
| realism | 64.68% | 53.18% | 18.59% | 87.78% | 12.22% | 81.41% |
| romanticism | 66.95% | 56.16% | 25.21% | 87.11% | 12.89% | 74.79% |
| **Mean** | **66.40%** | **55.96%** | **24.65%** | **87.26%** | **12.74%** | **75.35%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1334 | 7454 | 1123 | 3093 |
| realism | 807 | 7604 | 1059 | 3534 |
| romanticism | 1068 | 7638 | 1130 | 3168 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 88.64% |
| realism | 82.22% |
| romanticism | 83.79% |
| **Mean** | **84.88%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1453555868` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `100` |
| NPL | `[12288, 128, 64, 32, 1]` |


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
| Confusion Matrix | `engine\core\output\mlp\2026-07-14\16-55-39_070407\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-14_18-32-41_663.bin` | 6.04 MB |
| realism | `mlp__realism__2026-07-14_18-32-41_663.bin` | 6.04 MB |
| romanticism | `mlp__romanticism__2026-07-14_18-32-41_663.bin` | 6.04 MB |

Total size: `18.12 MB`


---

