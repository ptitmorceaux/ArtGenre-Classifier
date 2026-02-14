# ===== Configuration =====
CC       := gcc
LIB_NAME := libc
SRC_DIR  := src
INC_DIR  := include
OUT_DIR  := build
OBJ_DIR  := $(OUT_DIR)/objects
SPEC_DIR := specs


# ===== Détection Python =====
PYTHON := $(shell which python3 2>/dev/null || which python 2>/dev/null || which py 2>/dev/null || echo "")
ifeq ($(PYTHON),)
    PYTHON_AVAILABLE := 0
else
    PYTHON_AVAILABLE := 1
endif


# ===== Détection OS / Arch =====
ifeq ($(OS),Windows_NT)
    UNAME_S     := Windows
    UNAME_M     := $(PROCESSOR_ARCHITECTURE)
    EXT  := dll
    FLAG := -shared
else
    UNAME_S := $(shell uname -s)
    UNAME_M := $(shell uname -m)
    ifeq ($(UNAME_S),Darwin)
        EXT  := dylib
        FLAG := -dynamiclib -fPIC
    else
        EXT  := so
        FLAG := -shared -fPIC
    endif
endif


# ===== Fichiers =====
C_FILES   := $(wildcard $(SRC_DIR)/*.c)
H_FILES   := $(wildcard $(INC_DIR)/*.h)
OBJ_FILES := $(patsubst $(SRC_DIR)/%.c,$(OBJ_DIR)/%.o,$(C_FILES))
TARGET    := $(OUT_DIR)/$(LIB_NAME).$(EXT)

# ===== Flags =====
CFLAGS := -I$(INC_DIR) -Wall -Wextra -O2


# ===== Règle par défaut =====
all: info $(TARGET) generate-json

# Compilation : chaque .c devient un .o
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c $(H_FILES)
	@mkdir -p $(OBJ_DIR)
	@echo "  CC      $<"
	@$(CC) $(CFLAGS) -fPIC -c -o $@ $<

# Linkage final : on rassemble tous les .o pour créer la DLL
$(TARGET): $(OBJ_FILES)
	@echo "  LINK    $@"
	@$(CC) $(FLAG) -o $@ $^


# ===== Génération des JSON specs =====
generate-json:
ifeq ($(PYTHON_AVAILABLE),1)
	@echo "  GEN     JSON specs"
	@$(PYTHON) $(SPEC_DIR)/parser_c_to_json.py -i $(SRC_DIR) -o $(SPEC_DIR) -s DLLEXPORT || \
		(echo "Error: Failed to generate JSON specs. Check that the parser script is correct." && exit 1)
else
	@echo "Warning: Python not found. Skipping JSON generation."
	@echo "         Install Python to enable automatic JSON spec generation."
endif


# ===== Utils =====
clean:
	@rm -rf $(OUT_DIR) && rm -rf $(SPEC_DIR)/*.json

info:
	@echo "================================"
	@echo "OS        : $(UNAME_S)"
	@echo "Arch      : $(UNAME_M)"
	@echo "Extension : .$(EXT)"
	@echo "Compiler  : $(CC)"
ifeq ($(PYTHON_AVAILABLE),1)
	@echo "Python    : $(PYTHON)"
else
	@echo "Python    : NOT FOUND"
endif
	@echo "================================"

list:
	@echo "Sources : $(C_FILES)"
	@echo "Objects : $(OBJ_FILES)"


.PHONY: all clean info list generate-json