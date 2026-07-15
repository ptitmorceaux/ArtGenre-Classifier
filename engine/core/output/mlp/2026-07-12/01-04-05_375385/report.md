# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 47.12% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 67.20% | 61.63% | 44.16% | 79.10% | 20.90% | 55.84% |
| realism | 62.78% | 58.33% | 44.92% | 71.73% | 28.27% | 55.08% |
| romanticism | 64.26% | 61.22% | 52.48% | 69.96% | 30.04% | 47.52% |
| **Mean** | **64.75%** | **60.39%** | **47.19%** | **73.59%** | **26.41%** | **52.81%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1955 | 6784 | 1793 | 2472 |
| realism | 1950 | 6214 | 2449 | 2391 |
| romanticism | 2223 | 6134 | 2634 | 2013 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 68.09% | 59.84% | 33.97% | 85.71% | 14.29% | 66.03% |
| realism | 64.34% | 55.26% | 27.94% | 82.58% | 17.42% | 72.06% |
| romanticism | 66.43% | 58.50% | 35.72% | 81.27% | 18.73% | 64.28% |
| **Mean** | **66.29%** | **57.87%** | **32.54%** | **83.19%** | **16.81%** | **67.46%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1504 | 7351 | 1226 | 2923 |
| realism | 1213 | 7154 | 1509 | 3128 |
| romanticism | 1513 | 7126 | 1642 | 2723 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 92.99% |
| realism | 90.60% |
| romanticism | 91.26% |
| **Mean** | **91.62%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `2024` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `100` |
| NPL | `[12288, 128, 128, 1]` |


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
| Confusion Matrix | `engine\core\output\mlp\2026-07-12\01-04-05_375385\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-12_03-37-47_680.bin` | 6.06 MB |
| realism | `mlp__realism__2026-07-12_03-37-47_680.bin` | 6.06 MB |
| romanticism | `mlp__romanticism__2026-07-12_03-37-47_680.bin` | 6.06 MB |

Total size: `18.19 MB`


---

