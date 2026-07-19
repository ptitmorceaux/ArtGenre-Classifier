# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 40.74% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 60.49% | 56.92% | 45.74% | 68.10% | 31.90% | 54.26% |
| realism | 62.16% | 52.87% | 24.93% | 80.81% | 19.19% | 75.07% |
| romanticism | 58.84% | 57.00% | 51.72% | 62.27% | 37.73% | 48.28% |
| **Mean** | **60.49%** | **55.60%** | **40.80%** | **70.40%** | **29.60%** | **59.20%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2025 | 5841 | 2736 | 2402 |
| realism | 1082 | 7001 | 1662 | 3259 |
| romanticism | 2191 | 5460 | 3308 | 2045 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 58.49% | 58.01% | 56.52% | 59.51% | 40.49% | 43.48% |
| realism | 56.43% | 54.43% | 48.40% | 60.45% | 39.55% | 51.60% |
| romanticism | 52.00% | 54.82% | 62.91% | 46.73% | 53.27% | 37.09% |
| **Mean** | **55.64%** | **55.75%** | **55.94%** | **55.56%** | **44.44%** | **44.06%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2502 | 5104 | 3473 | 1925 |
| realism | 2101 | 5237 | 3426 | 2240 |
| romanticism | 2665 | 4097 | 4671 | 1571 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 56.44% |
| realism | 53.84% |
| romanticism | 56.35% |
| **Mean** | **55.55%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `42` |
| Type | `linear` |
| Alpha | `0.001` |
| Epochs | `100` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `29652` |
| Total samples Test | `13004` |
| Limit per category | `9884` |
| Train positive ratio | `0.50` |
| Normalization | `standard` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 9884 | 4427 |
| realism | 9884 | 4341 |
| romanticism | 9884 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 9884 | 4942 | 4942 | **19768** |
| **realism** | 4942 | 9884 | 4942 | **19768** |
| **romanticism** | 4942 | 4942 | 9884 | **19768** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine/core/output/linear/2026-07-19/23-32-53_564151/confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| romanticism | `linear__romanticism__2026-07-19_23-33-03_602.bin` | 0.00 MB |
| impressionism | `linear__impressionism__2026-07-19_23-33-03_602.bin` | 0.00 MB |
| realism | `linear__realism__2026-07-19_23-33-03_602.bin` | 0.00 MB |

Total size: `0.01 MB`


---

