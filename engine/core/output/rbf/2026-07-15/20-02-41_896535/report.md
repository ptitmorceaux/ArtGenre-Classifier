# 0. Evaluation/0. Final Multiclass Result


## Multiclass Global Metrics

| Metric | Value |
|---|---:|
| Top-1 Accuracy | 33.97% |

## Final Multiclass Result (Argmax)

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 64.35% | 53.33% | 18.82% | 87.85% | 12.15% | 81.18% |
| realism | 44.86% | 48.93% | 61.16% | 36.70% | 63.30% | 38.84% |
| romanticism | 58.74% | 49.23% | 21.95% | 76.51% | 23.49% | 78.05% |
| **Mean** | **55.98%** | **50.50%** | **33.98%** | **67.02%** | **32.98%** | **66.02%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 833 | 7535 | 1042 | 3594 |
| realism | 2655 | 3179 | 5484 | 1686 |
| romanticism | 930 | 6708 | 2060 | 3306 |


---

# 0. Evaluation/1. Individual Models


# Individual Models

| Category | Exact Match Accuracy | Balanced Accuracy | TPR | TNR | FPR | FNR |
|---|---:|---:|---:|---:|---:|---:|
| impressionism | 63.70% | 58.45% | 42.01% | 74.89% | 25.11% | 57.99% |
| realism | 43.26% | 49.81% | 69.55% | 30.08% | 69.92% | 30.45% |
| romanticism | 53.55% | 47.44% | 29.91% | 64.97% | 35.03% | 70.09% |
| **Mean** | **53.50%** | **51.90%** | **47.16%** | **56.65%** | **43.35%** | **52.84%** |

## Confusion Counts

| Category | TP | TN | FP | FN |
|---|---:|---:|---:|---:|
| impressionism | 1860 | 6423 | 2154 | 2567 |
| realism | 3019 | 2606 | 6057 | 1322 |
| romanticism | 1267 | 5697 | 3071 | 2969 |


---

# 1. Training/Final Train Accuracy


# Final Train Accuracy

| Category | Accuracy |
|---|---:|
| impressionism | 60.00% |
| realism | 53.33% |
| romanticism | 54.00% |
| **Mean** | **55.78%** |


---

# 2. Experiment/0. Model


# Model

| Parameter | Value |
|---|---|
| Seed | `42` |
| Type | `rbf` |
| Alpha | `0.01` |
| Epochs | `10` |


---

# 2. Experiment/1. Dataset


# Dataset

| Parameter | Value |
|---|---|
| Total samples Train (chargées) | `150` |
| Total samples Test | `13004` |
| Limit per category | `50` |
| Train positive ratio | `désactivé (-1)` |
| Normalization | `per_column` |

## Categories (images chargées)

| Category | Images Train | Images Test |
|---|---:|---:|
| impressionism | 50 | 4427 |
| realism | 50 | 4341 |
| romanticism | 50 | 4236 |

## Répartition par modèle (One-vs-All)

| Modèle \ Catégorie utilisée | impressionism | realism | romanticism | **Total dataset modèle** |
|---|---:|---:|---:|---:|
| **impressionism** | 50 | 50 | 50 | **150** |
| **realism** | 50 | 50 | 50 | **150** |
| **romanticism** | 50 | 50 | 50 | **150** |


---

# 2. Experiment/2. Artifacts


# Artifacts

| File | Path |
|---|---|
| Config | `./config.json` |
| Confusion Matrix | `engine\core\output\rbf\2026-07-15\20-02-41_896535\confusion_matrix_test.png` |


# Models

| Category | File | Size |
|---|---|---:|
| impressionism | `rbf__impressionism__2026-07-15_20-02-53_279.bin` | 0.75 MB |
| realism | `rbf__realism__2026-07-15_20-02-53_279.bin` | 0.75 MB |
| romanticism | `rbf__romanticism__2026-07-15_20-02-53_279.bin` | 0.75 MB |

Total size: `2.25 MB`


---

