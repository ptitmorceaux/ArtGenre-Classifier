# Download du Dataset

On enregistre pas de Dataset dans github (trop lourd) !

# Convention

```
│   README.md
│   separate.py
│
├───all
│   │   impressionism_clean.csv
│   │   realism_clean.csv
│   │   romanticism_clean.csv
│   │
│   ├───256x256
│   │   ├───impressionism/
│   │   ├───realism/
│   │   └───romanticism/
│   └───64x64
│       ├───impressionism/
│       ├───realism/
│       └───romanticism/
├───test
│   │   impressionism_clean.csv
│   │   realism_clean.csv
│   │   romanticism_clean.csv
│   │
│   ├───256x256
│   │   ├───impressionism/
│   │   ├───realism/
│   │   └───romanticism/
│   └───64x64
│       ├───impressionism/
│       ├───realism/
│       └───romanticism/
└───train
    │   impressionism_clean.csv
    │   realism_clean.csv
    │   romanticism_clean.csv
    │
    ├───256x256
    │   ├───impressionism/
    │   ├───realism/
    │   └───romanticism/
    └───64x64
        ├───impressionism/
        ├───realism/
        └───romanticism/
```

# Separation
```
Genres détectés   : impressionism, realism, romanticism
Résolutions       : 256x256, 64x64
Ratio train/test  : 70% / 30%
Seed              : 42
Mode              : MOVE

=== Genre: impressionism ===
  Lignes CSV total       : 14758
  Valides (toutes rés.)  : 14758
  Invalides / ignorées   : 0
  -> 10331 train / 4427 test (par résolution)

=== Genre: realism ===
  Lignes CSV total       : 14471
  Valides (toutes rés.)  : 14471
  Invalides / ignorées   : 0
  -> 10130 train / 4341 test (par résolution)

=== Genre: romanticism ===
  Lignes CSV total       : 14120
  Valides (toutes rés.)  : 14120
  Invalides / ignorées   : 0
  -> 9884 train / 4236 test (par résolution)

=== Résumé global ===
Total train : 30345
Total test  : 13004
Total       : 43349
```