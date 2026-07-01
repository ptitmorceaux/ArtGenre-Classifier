# Installation des dépendances

## Windows (MSYS2)

```sh
pacman -Syu
# Fermer puis rouvrir le terminal MSYS2 si demandé
pacman -Syu

pacman -S mingw-w64-x86_64-gcc mingw-w64-x86_64-openblas
```

## Linux (Debian / Ubuntu)

```sh
sudo apt update -y && sudo apt upgrade -y
sudo apt install -y build-essential libopenblas-dev
```

## macOS (Homebrew)

```sh
brew update
brew install openblas
```

---

# Compiler avec OpenBLAS

## Windows (MSYS2)

```sh
gcc test_lapack.c -o test_lapack -lopenblas
```

## Linux

```sh
gcc test_lapack.c -o test_lapack -lopenblas
```

## macOS

```sh
gcc test_lapack.c -o test_lapack -lopenblas
```

> Dans la plupart des cas, la même commande fonctionne sur les trois systèmes si OpenBLAS est installé dans un emplacement standard.

Si Homebrew n'est pas trouvé automatiquement (Mac avec Apple Silicon) :

```sh
gcc test_lapack.c -o test_lapack \
-I/opt/homebrew/include \
-L/opt/homebrew/lib \
-lopenblas
```

---

# Chemins d'installation

## Windows (MSYS2)

* Exécutables :
```
C:\msys64\mingw64\bin
```

* Bibliothèques :
```
C:\msys64\mingw64\lib
```

* En-têtes :
```
C:\msys64\mingw64\include
```

## Linux

* Bibliothèques :
```
/usr/lib/x86_64-linux-gnu/
/usr/lib/
```

* En-têtes :
```
/usr/include/
```

## macOS (Homebrew)

### Apple Silicon (M1/M2/M3...) :

* Bibliothèques :
```
/opt/homebrew/lib
```

* En-têtes :
```
/opt/homebrew/include
```

### Mac Intel :

* Bibliothèques :
```
/usr/local/lib
```

* En-têtes :
```
/usr/local/include
```