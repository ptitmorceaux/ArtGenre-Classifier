# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 44.06% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 52.90% | 62.33% | 91.89% | 32.77% | 67.23% | 8.11% |
| realism | 66.73% | 54.35% | 17.12% | 91.58% | 8.42% | 82.88% |
| romanticism | 68.49% | 56.39% | 21.67% | 91.10% | 8.90% | 78.33% |
| **Mean** | **62.70%** | **57.69%** | **43.56%** | **71.82%** | **28.18%** | **56.44%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 4068 | 2811 | 5766 | 359 |
| realism | 743 | 7934 | 729 | 3598 |
| romanticism | 918 | 7988 | 780 | 3318 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 42.03% | 55.53% | 97.83% | 13.23% | 86.77% | 2.17% |
| realism | 47.66% | 56.57% | 83.37% | 29.77% | 70.23% | 16.63% |
| romanticism | 40.63% | 54.44% | 94.07% | 14.80% | 85.20% | 5.93% |
| **Mean** | **43.44%** | **55.51%** | **91.76%** | **19.27%** | **80.73%** | **8.24%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 4331 | 1135 | 7442 | 96 |
| realism | 3619 | 2579 | 6084 | 722 |
| romanticism | 3985 | 1298 | 7470 | 251 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 57.68% |
| realism | 52.64% |
| romanticism | 54.17% |
| **Mean** | **54.83%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `2024` |
| Type | `rbf` |
| Alpha | `0.001` |
| Epochs | `75` |


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
| Confusion Matrix | `engine/core/output/rbf/2026-07-19/23-15-40_648299/confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| romanticism | `rbf__romanticism__2026-07-19_23-16-51_602.bin` | 0.07 MB |
| impressionism | `rbf__impressionism__2026-07-19_23-16-51_602.bin` | 0.07 MB |
| realism | `rbf__realism__2026-07-19_23-16-51_602.bin` | 0.07 MB |

Total size: `0.21 MB`


---

