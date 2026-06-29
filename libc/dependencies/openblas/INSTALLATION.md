## Installer la lib avec pacman (MSYS2)

```sh
pacman -Syu && pacman -Syu && pacman -S mingw-w64-x86_64-openblas
```

### Compiler avec la lib

```
gcc test_lapack.c -o test_lapack -lopenblas
```

### INFO

Il faut mettre le binaire d'openblas dans le dossier build