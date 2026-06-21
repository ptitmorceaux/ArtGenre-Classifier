import platform
from pathlib import Path
from PIL import Image

from engine.interop.mlp import MLP
from engine.interop.loader import _LibLoader
# from engine.interop.linearModel import LinearModel

# --- 1. DÉFINITION DES CHEMINS ---
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
LIB_NAME = 'libc.dll' if platform.system() == 'Windows' else 'libc.so'

LIB_FOLDER = str(PROJECT_ROOT / 'libc')
BUILD_FOLDER = str(PROJECT_ROOT / 'libc' / 'build')
SPECS_FOLDER = str(PROJECT_ROOT / 'libc' / 'specs')

try:
    loader = _LibLoader()
    loader.loadLibrary(LIB_NAME, LIB_FOLDER, BUILD_FOLDER, SPECS_FOLDER)
    print(f"[MOTEUR C] Librairie {LIB_NAME} et Specs JSON prêtes à l'emploi !")
except Exception as e:
    print(f"[ERREUR C] Échec du chargement : {e}")

class ArtClassifierService:
    @staticmethod
    def process_image(image_file):
        img = Image.open(image_file).convert('RGB')
        img = img.resize((64, 64))
        flat_data = [pixel_val / 255.0 for pixel in img.getdata() for pixel_val in pixel]
        return flat_data

    @classmethod
    def predict(cls, model_type, image_file):
        input_data = cls.process_image(image_file)
        input_size = len(input_data)

        if model_type == 'mlp':
            model = MLP([input_size, 128, 3])
            
            # --- LA PRÉDICTION C ---
            prediction = model.predict(input_data, is_classification=True)
            model.close()
            
            return {
                'model_used': 'Perceptron Multi-Couches (C)',
                'raw_prediction': prediction,
                'input_size': input_size
            }
        elif model_type == 'linear':
            return {'error': "Le modèle linéaire n'est pas encore branché."}
        else:
            raise ValueError("Modèle inconnu.")