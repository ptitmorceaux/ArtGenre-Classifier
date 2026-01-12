# ===== Compilateur =====
CC ?= gcc

# ===== Détection OS / Arch =====
ifeq ($(OS),Windows_NT)
    UNAME_S := Windows
    UNAME_M := $(PROCESSOR_ARCHITECTURE)
    SHARED_EXT := dll
    SHARED_FLAG := -shared
else
    UNAME_S := $(shell uname -s)
    UNAME_M := $(shell uname -m)
    ifeq ($(UNAME_S),Darwin)
        SHARED_EXT := dylib
        SHARED_FLAG := -dynamiclib -fPIC
    else
        SHARED_EXT := so
        SHARED_FLAG := -shared -fPIC
    endif
endif

# ===== Dossiers =====
SRC_DIR := libc/src
OUT_DIR := libc/$(SHARED_EXT)

# ===== Fichiers =====
C_FILES := $(wildcard $(SRC_DIR)/*.c)
LIBS := $(patsubst $(SRC_DIR)/%.c,$(OUT_DIR)/lib%.$(SHARED_EXT),$(C_FILES))

# ===== Règle par défaut =====
all: info $(LIBS)

# ===== Build lib dynamique =====
$(OUT_DIR)/lib%.$(SHARED_EXT): $(SRC_DIR)/%.c
	@mkdir -p $(OUT_DIR)
	$(CC) $(SHARED_FLAG) -o $@ $<

# ===== Infos =====
info:
	@echo "OS        : $(UNAME_S)"
	@echo "Arch      : $(UNAME_M)"
	@echo "Extension : .$(SHARED_EXT)"
	@echo "Compiler  : $(CC)"

# ===== Nettoyage =====
clean:
	@rm -rf $(OUT_DIR)

# ===== Listing =====
list:
	@echo "Sources:"
	@echo $(C_FILES)
	@echo "Libs:"
	@echo $(LIBS)

.PHONY: all clean list info
