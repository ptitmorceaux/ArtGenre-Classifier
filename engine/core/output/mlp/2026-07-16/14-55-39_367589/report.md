# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 45.27% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 64.48% | 60.04% | 46.13% | 73.95% | 26.05% | 53.87% |
| realism | 61.07% | 56.27% | 41.83% | 70.71% | 29.29% | 58.17% |
| romanticism | 64.99% | 60.57% | 47.90% | 73.24% | 26.76% | 52.10% |
| **Mean** | **63.51%** | **58.96%** | **45.29%** | **72.64%** | **27.36%** | **54.71%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2042 | 6343 | 2234 | 2385 |
| realism | 1816 | 6126 | 2537 | 2525 |
| romanticism | 2029 | 6422 | 2346 | 2207 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 66.99% | 58.07% | 30.13% | 86.01% | 13.99% | 69.87% |
| realism | 64.83% | 54.72% | 24.33% | 85.12% | 14.88% | 75.67% |
| romanticism | 67.26% | 57.72% | 30.36% | 85.08% | 14.92% | 69.64% |
| **Mean** | **66.36%** | **56.84%** | **28.27%** | **85.40%** | **14.60%** | **71.73%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1334 | 7377 | 1200 | 3093 |
| realism | 1056 | 7374 | 1289 | 3285 |
| romanticism | 1286 | 7460 | 1308 | 2950 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 86.24% |
| realism | 84.28% |
| romanticism | 85.60% |
| **Mean** | **85.37%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1337` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `40` |
| NPL | `[1024, 64, 32, 1]` |


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
| Confusion Matrix | `engine\core\output\mlp\2026-07-16\14-55-39_367589\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-16_14-58-14_354.bin` | 0.26 MB |
| realism | `mlp__realism__2026-07-16_14-58-14_354.bin` | 0.26 MB |
| romanticism | `mlp__romanticism__2026-07-16_14-58-14_354.bin` | 0.26 MB |

Total size: `0.78 MB`


---

