# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 43.11% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 64.45% | 61.85% | 53.72% | 69.99% | 30.01% | 46.28% |
| realism | 62.15% | 53.28% | 26.61% | 79.96% | 20.04% | 73.39% |
| romanticism | 59.62% | 56.86% | 48.94% | 64.78% | 35.22% | 51.06% |
| **Mean** | **62.07%** | **57.33%** | **43.09%** | **71.58%** | **28.42%** | **56.91%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2378 | 6003 | 2574 | 2049 |
| realism | 1155 | 6927 | 1736 | 3186 |
| romanticism | 2073 | 5680 | 3088 | 2163 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 61.37% | 61.31% | 61.12% | 61.50% | 38.50% | 38.88% |
| realism | 37.03% | 51.69% | 95.81% | 7.57% | 92.43% | 4.19% |
| romanticism | 56.53% | 56.57% | 56.70% | 56.44% | 43.56% | 43.30% |
| **Mean** | **51.64%** | **56.53%** | **71.21%** | **41.84%** | **58.16%** | **28.79%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 2706 | 5275 | 3302 | 1721 |
| realism | 4159 | 656 | 8007 | 182 |
| romanticism | 2402 | 4949 | 3819 | 1834 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 60.54% |
| realism | 52.31% |
| romanticism | 57.23% |
| **Mean** | **56.69%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `2024` |
| Type | `rbf` |
| Alpha | `0.0001` |
| Epochs | `70` |


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
| Confusion Matrix | `engine/core/output/rbf/2026-07-19/23-28-44_602554/confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| realism | `rbf__realism__2026-07-19_23-29-52_835.bin` | 0.06 MB |
| impressionism | `rbf__impressionism__2026-07-19_23-29-52_835.bin` | 0.06 MB |
| romanticism | `rbf__romanticism__2026-07-19_23-29-52_835.bin` | 0.06 MB |

Total size: `0.19 MB`


---

