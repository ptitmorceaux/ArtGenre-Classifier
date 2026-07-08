import os
import glob
from PIL import Image

from engine.interop.storage import Storage
from engine.core.config import CONFIG, CATEGORIES

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

class ArtClassifierService:
    @staticmethod
    def process_image(image_file):
        img = Image.open(image_file).convert('RGB')
        img = img.resize((64, 64))
        flat_data = [pixel_val / 255.0 for pixel in img.getdata() for pixel_val in pixel]
        return flat_data

    @staticmethod
    def get_latest_model_path(model_type, category):
        """Récupère le chemin du modèle binaire le plus récent pour un type et une catégorie donnés."""
        models_dir = os.path.join(BASE_DIR, CONFIG["output"]["models"])
        
        pattern = os.path.join(models_dir, f"{model_type}__{category}__*.bin")
        list_of_files = glob.glob(pattern)
        
        if not list_of_files:
            return None
            
        return max(list_of_files, key=os.path.getctime)

    @staticmethod
    def predict(model_type, image_file):
        input_data = ArtClassifierService.process_image(image_file)
        input_size = len(input_data)
        
        predictions = {}
        
        for category in CATEGORIES.keys():
            model_path = ArtClassifierService.get_latest_model_path(model_type, category)
            
            if not model_path:
                return {'error': f"Modèle introuvable pour '{model_type}' et '{category}'. Dossier cherché : {os.path.join(BASE_DIR, CONFIG['output']['models'])}"}
            
            model, scaler = Storage["load"](model_path)
            
            normalized_data = scaler.transform(input_data)
            raw_pred = model.predict(normalized_data, is_classification=True)
            
            if isinstance(raw_pred, list):
                predictions[category] = float(raw_pred[0])
            else:
                predictions[category] = float(raw_pred)
                
            if hasattr(model, 'close'):
                model.close()
                
        best_category = max(predictions, key=predictions.get)

        return {
            'model_used': f"{'Perceptron Multi-Couches' if model_type == 'mlp' else 'Modèle Linéaire'} (C)",
            'best_category': best_category,
            'raw_prediction': predictions,
            'input_size': input_size
        }