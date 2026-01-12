# Compilateur
CC = gcc

# Dossiers
SRC_DIR = libc
DLL_DIR = libc/dll

# Trouver tous les fichiers .c dans le dossier c/
C_FILES = $(wildcard $(SRC_DIR)/*.c)

# Générer les noms des DLL correspondantes
DLLS = $(patsubst $(SRC_DIR)/%.c,$(DLL_DIR)/%.dll,$(C_FILES))

# Règle par défaut : construire toutes les DLL
all: $(DLLS)

# Règle pour créer une DLL à partir d'un fichier .c
$(DLL_DIR)/%.dll: $(SRC_DIR)/%.c
	@mkdir -p $(DLL_DIR)
	$(CC) -shared -o $@ $<

# Nettoyer les DLL générées
clean:
	rm -f $(DLL_DIR)/*.dll

# Afficher la liste des DLL qui seront générées
list:
	@echo "Fichiers C trouvés:"
	@echo $(C_FILES)
	@echo "DLLs qui seront générées:"
	@echo $(DLLS)

.PHONY: all clean list
