# libc

Ce dossier contient les bibliothèques dynamiques C du projet.

## Structure

### 📁 `src/`
Contient les fichiers sources C (`.c`) qui implémentent les fonctions de la bibliothèque.

**Exemple:** `mathlib.c` implémente les fonctions mathématiques (add, sub, mult, div, power).

### 📁 `specs/`
Contient les fichiers de spécification JSON (`.json`) qui décrivent les signatures des fonctions de chaque bibliothèque.

**Format:**
```json
{
    "nom_fonction": {
        "argtypes": ["type1", "type2", ...],
        "restype": "type_retour"
    }
}
```

Ces spécifications permettent au wrapper Python de charger correctement les fonctions C via `ctypes` en connaissant les types d'arguments et de retour.

### 📁 `build/`
Contient les bibliothèques dynamiques compilées à partir des sources.

**Extension selon l'OS:**
- **Windows:** `.dll`
- **Linux:** `.so`
- **macOS:** `.dylib`

## Processus de compilation

Le [Makefile](../Makefile) à la racine du projet gère la compilation:

1. **Détection de l'OS** pour choisir l'extension appropriée
2. **Compilation** des fichiers `.c` de `src/` en bibliothèques dynamiques
3. **Placement** des bibliothèques compilées dans le dossier `build`

```bash
# Compiler toutes les bibliothèques
make -C libc/

# Nettoyer les bibliothèques compilées
make -C libc/ clean
```

## Workflow

```
src/mathlib.c  ──────────────┐
                             │ (Makefile)
                             ↓
                 build/mathlib.dll   (Windows)
                 build/mathlib.so     (Linux)
                 build/mathlib.dylib (macOS)
                             │
                             │ (loader.py)
                             ↓
specs/mathlib.json ─────→ wrapper Python
```

1. **src/** : Code source C
2. **Makefile** : Compile en bibliothèque dynamique
3. **build/dll||so||dylib** : Bibliothèque compilée
4. **specs/** : Spécifications pour le chargement Python
5. **api/wrappers/** : Wrapper Python qui utilise specs + dll||so||dylib
