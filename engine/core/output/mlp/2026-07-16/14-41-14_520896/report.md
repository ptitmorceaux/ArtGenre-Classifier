# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 45.89% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 65.89% | 60.43% | 43.33% | 77.53% | 22.47% | 56.67% |
| realism | 60.94% | 57.59% | 47.52% | 67.66% | 32.34% | 52.48% |
| romanticism | 64.95% | 60.28% | 46.88% | 73.68% | 26.32% | 53.12% |
| **Mean** | **63.92%** | **59.43%** | **45.91%** | **72.96%** | **27.04%** | **54.09%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1918 | 6650 | 1927 | 2509 |
| realism | 2063 | 5861 | 2802 | 2278 |
| romanticism | 1986 | 6460 | 2308 | 2250 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 66.26% | 57.30% | 29.23% | 85.38% | 14.62% | 70.77% |
| realism | 64.17% | 55.77% | 30.50% | 81.05% | 18.95% | 69.50% |
| romanticism | 66.93% | 58.71% | 35.10% | 82.31% | 17.69% | 64.90% |
| **Mean** | **65.79%** | **57.26%** | **31.61%** | **82.91%** | **17.09%** | **68.39%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1294 | 7323 | 1254 | 3133 |
| realism | 1324 | 7021 | 1642 | 3017 |
| romanticism | 1487 | 7217 | 1551 | 2749 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 92.40% |
| realism | 89.75% |
| romanticism | 91.98% |
| **Mean** | **91.38%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `1337` |
| Type | `mlp` |
| Alpha | `0.001` |
| Epochs | `50` |
| NPL | `[1024, 128, 32, 1]` |


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
| Confusion Matrix | `engine\core\output\mlp\2026-07-16\14-41-14_520896\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `mlp__impressionism__2026-07-16_14-48-45_684.bin` | 0.52 MB |
| realism | `mlp__realism__2026-07-16_14-48-45_684.bin` | 0.52 MB |
| romanticism | `mlp__romanticism__2026-07-16_14-48-45_684.bin` | 0.52 MB |

Total size: `1.55 MB`


---

