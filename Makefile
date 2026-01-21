# ===== Configuration =====
CC       := gcc
LIB_NAME := libc
SRC_DIR  := libc/src
INC_DIR  := libc/include
OUT_DIR  := libc/build
OBJ_DIR  := $(OUT_DIR)/objects


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
all: info $(TARGET)

# Compilation : chaque .c devient un .o
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c $(H_FILES)
	@mkdir -p $(OBJ_DIR)
	@echo "  CC      $<"
	@$(CC) $(CFLAGS) -fPIC -c -o $@ $<

# Linkage final : on rassemble tous les .o pour créer la DLL
$(TARGET): $(OBJ_FILES)
	@echo "  LINK    $@"
	@$(CC) $(FLAG) -o $@ $^


# ===== Utils =====
clean:
	@rm -rf $(OUT_DIR)

info:
	@echo "================================"
	@echo "OS        : $(UNAME_S)"
	@echo "Arch      : $(UNAME_M)"
	@echo "Extension : .$(EXT)"
	@echo "Compiler  : $(CC)"
	@echo "================================"

list:
	@echo "Sources : $(C_FILES)"
	@echo "Objects : $(OBJ_FILES)"


.PHONY: all clean info list