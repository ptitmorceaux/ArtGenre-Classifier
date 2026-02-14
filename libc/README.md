# libc

Ce dossier contient la bibliothèque dynamique C du projet, qui regroupe toutes les fonctions natives utilisées pour les calculs intensifs.

## Structure

### 📁 `src/`
Contient les fichiers sources C (`.c`) qui implémentent les fonctions de la bibliothèque.

**Modules disponibles:**
- `math.c` : Fonctions mathématiques de base (add, sub, mult, div, power)
- `array.c` : Opérations sur les tableaux
- `linearModel.c` : Implémentation du modèle linéaire
- `utils.c` : Fonctions utilitaires

### 📁 `include/`
Contient les fichiers d'en-tête (`.h`) partagés entre les modules.

### 📁 `specs/`
Contient les fichiers de spécification JSON (`.json`) qui décrivent les signatures des fonctions pour chaque module.

**Format:**
```json
{
    "nom_fonction": {
        "argtypes": ["type1", "type2", ...],
        "restype": "type_retour"
    }
}
```

**Important:** Ces spécifications JSON sont **essentielles** pour le wrapper Python (`ctypes`). Elles permettent de charger correctement les fonctions C en connaissant les types d'arguments et de retour attendus.

**Génération automatique:** Les fichiers JSON sont générés automatiquement par `parser_c_to_json.py` lors de la compilation. Ce script analyse les fichiers C et extrait automatiquement les signatures des fonctions marquées avec `DLLEXPORT`.

### 📁 `build/`
Contient la bibliothèque dynamique compilée (`libc.dll`/`.so`/`.dylib`) et les fichiers objets intermédiaires.

**Extension selon l'OS:**
- **Windows:** `libc.dll`
- **Linux:** `libc.so`
- **macOS:** `libc.dylib`

## Processus de compilation

Le [Makefile](Makefile) gère la compilation et la génération des specs:

1. **Détection de l'OS** et de l'architecture
2. **Compilation** de chaque fichier `.c` en objet `.o`
3. **Linkage** de tous les objets en une seule bibliothèque dynamique `libc.dll`/`.so`/`.dylib`
4. **Génération automatique** des fichiers JSON specs via `parser_c_to_json.py`

```bash
# Compiler la bibliothèque et générer les specs JSON
make

# Nettoyer la compilation et les specs générées
make clean

# Afficher les informations de compilation
make info
```

## Workflow

```
src/*.c + include/*.h
    │
    │ (Makefile: compilation)
    ↓
build/objects/*.o
    │
    │ (Makefile: linkage)
    ↓
build/libc.dll / .so / .dylib
    │
    │ (parser_c_to_json.py)
    ↓
specs/*.json ──────────────┐
    │                      │
    │ (loader.py)          │
    ↓                      ↓
engine/interop/*.py ← Wrappers Python (ctypes)
```

1. **src/** : Code source C avec annotations DLLEXPORT
2. **Makefile** : Compile tous les modules en une bibliothèque unique
3. **build/libc.{dll|so|dylib}** : Bibliothèque compilée contenant toutes les fonctions
4. **parser_c_to_json.py** : Génère automatiquement les specs JSON
5. **specs/*.json** : Spécifications pour ctypes (un JSON par module)
6. **engine/interop/** : Wrappers Python qui utilisent specs + bibliothèque via ctypes
