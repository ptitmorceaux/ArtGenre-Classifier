from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
]

# Chemin vers la bibliothèque partagée compilée (.so sur Linux/WSL2 ou .dll sur Windows)
# Permet à loader.py de s'adapter nativement à l'environnement
SHARED_LIBRARY_PATH = BASE_DIR / 'libc' / 'bin' / 'libshared_models.so'