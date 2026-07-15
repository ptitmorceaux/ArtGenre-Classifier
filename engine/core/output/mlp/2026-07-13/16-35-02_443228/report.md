# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 46.82% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 67.09% | 62.69% | 48.90% | 76.48% | 23.52% | 51.10% |
| realism | 62.22% | 57.24% | 42.27% | 72.22% | 27.78% | 57.73% |
| romanticism | 64.32% | 60.44% | 49.29% | 71.58% | 28.42% | 50.71% |
| **Mean** | **64.54%** | **60.12%** | **46.82%** | **73.43%** | **26.57%** | **53.18%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2165 | 6560 | 2017 | 2262 |
| realism | 1835 | 6256 | 2407 | 2506 |
| romanticism | 2088 | 6276 | 2492 | 2148 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 68.23% | 59.56% | 32.39% | 86.72% | 13.28% | 67.61% |
| realism | 65.01% | 54.18% | 21.58% | 86.77% | 13.23% | 78.42% |
| romanticism | 67.36% | 55.74% | 22.40% | 89.07% | 10.93% | 77.60% |
| **Mean** | **66.86%** | **56.49%** | **25.46%** | **87.52%** | **12.48%** | **74.54%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1434 | 7438 | 1139 | 2993 |
| realism | 937 | 7517 | 1146 | 3404 |
| romanticism | 949 | 7810 | 958 | 3287 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 86.91% |
| realism | 83.19% |
| romanticism | 82.54% |
| **Mean** | **84.21%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1337` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `100` |
| NPL | `[12288, 128, 128, 128, 1]` |


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
| Confusion Matrix | `engine\core\output\mlp\2026-07-13\16-35-02_443228\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-13_23-52-00_862.bin` | 6.13 MB |
| realism | `mlp__realism__2026-07-13_23-52-00_862.bin` | 6.13 MB |
| romanticism | `mlp__romanticism__2026-07-13_23-52-00_862.bin` | 6.13 MB |

Total size: `18.38 MB`


---

