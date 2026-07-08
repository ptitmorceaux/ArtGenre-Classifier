from PIL import Image

import os
import glob
import io
import base64

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use('Agg')

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
        models_dir = os.path.join(BASE_DIR, CONFIG["output"]["models"])
        pattern = os.path.join(models_dir, f"{model_type}__{category}__*.bin")
        list_of_files = glob.glob(pattern)
        if not list_of_files:
            return None
        return max(list_of_files, key=os.path.getctime)

    @staticmethod
    def generate_matplotlib_chart(predictions, title):
        """Génère un graphique à barres des scores bruts et le retourne en Base64."""
        plt.figure(figsize=(7, 4))
        categories = list(predictions.keys())
        scores = list(predictions.values())
        
        colors = ['#2ecc71' if s > 0 else '#e74c3c' for s in scores]
        
        bars = plt.bar(categories, scores, color=colors)
        plt.axhline(0, color='black', linewidth=1)
        plt.title(title)
        plt.ylabel("Score brut (Dot Product / Raw Output)")
        
        plt.tight_layout()

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        image_base64 = base64.b64encode(buf.read()).decode('utf-8')
        plt.close()
        
        return image_base64

    @staticmethod
    def predict(model_type, image_file):
        input_data = ArtClassifierService.process_image(image_file)
        input_size = len(input_data)
        predictions = {}
        
        for category in CATEGORIES.keys():
            model_path = ArtClassifierService.get_latest_model_path(model_type, category)
            
            if not model_path:
                return {'error': f"Modèle introuvable pour '{model_type}' et '{category}'."}
            
            model, scaler = Storage["load"](model_path)
            normalized_data = scaler.transform(input_data)

            raw_pred = model.predict(normalized_data, is_classification=False)
            
            if isinstance(raw_pred, list):
                predictions[category] = float(raw_pred[0])
            else:
                predictions[category] = float(raw_pred)
                
            if hasattr(model, 'close'):
                model.close()
                
        best_category = max(predictions, key=predictions.get)

        chart_base64 = ArtClassifierService.generate_matplotlib_chart(
            predictions, 
            f"Cheminement de décision - Modèle {model_type.upper()}"
        )

        return {
            'model_used': f"{'Perceptron Multi-Couches' if model_type == 'mlp' else 'Modèle Linéaire'} (C)",
            'best_category': best_category,
            'raw_prediction': predictions,
            'chart_base64': chart_base64,
            'input_size': input_size
        }
