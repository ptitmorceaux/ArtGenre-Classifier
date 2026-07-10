# interface/backend/api/services.py
from PIL import Image
import os
import io
import glob
import base64
import json
import matplotlib
import matplotlib.pyplot as plt

from .models import TrainingSession
from engine.interop.storage import Storage
from engine.core.config import CATEGORIES

matplotlib.use('Agg')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

class ArtClassifierService:
    @staticmethod
    def process_image(image_file):
        img = Image.open(image_file).convert('RGB')
        img = img.resize((64, 64))
        flat_data = [pixel_val / 255.0 for pixel in img.getdata() for pixel_val in pixel]
        return flat_data

    @staticmethod
    def generate_matplotlib_chart(predictions, title):
        plt.figure(figsize=(7, 4))
        categories = list(predictions.keys())
        scores = list(predictions.values())
        colors = ['#2ecc71' if s > 0 else '#e74c3c' for s in scores]
        plt.bar(categories, scores, color=colors)
        plt.axhline(0, color='black', linewidth=1)
        plt.title(title)
        plt.ylabel("Score brut (Dot Product)")
        plt.tight_layout()
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        image_base64 = base64.b64encode(buf.read()).decode('utf-8')
        plt.close()
        return image_base64

    @staticmethod
    def predict(session_id, image_file):
        # On cherche le fichier config.json correspondant à la session_id dans le dossier output
        output_dir = os.path.join(BASE_DIR, "engine", "core", "output")
        config_paths = glob.glob(os.path.join(output_dir, "**", session_id, "config.json"), recursive=True)
        
        if not config_paths:
            return {'error': f"Configuration introuvable pour la session {session_id}."}
            
        with open(config_paths[0], 'r') as f:
            config_data = json.load(f)
            
        model_type = config_data.get("model", {}).get("type", "unknown")
        saved_models = config_data.get("model", {}).get("saved_models", {})
        
        input_data = ArtClassifierService.process_image(image_file)
        input_size = len(input_data)
        predictions = {}
        
        # On charge les modèles .bin indiqués par le JSON
        for category in CATEGORIES.keys():
            if category not in saved_models:
                return {'error': f"Modèle introuvable pour la catégorie '{category}'."}
                
            model_path = os.path.join(BASE_DIR, saved_models[category])
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
            predictions, f"Cheminement de décision - {model_type.upper()}"
        )

        return {
            'model_used': f"{'Perceptron Multi-Couches' if model_type == 'mlp' else 'Modèle Linéaire'} (C)",
            'best_category': best_category,
            'raw_prediction': predictions,
            'chart_base64': chart_base64,
            'input_size': input_size
        }

class ModelSyncService:
    @staticmethod
    def sync_models_to_db():
        """Scanne les config.json générés pour peupler la BDD."""
        output_dir = os.path.join(BASE_DIR, "engine", "core", "output")
        config_files = glob.glob(os.path.join(output_dir, "**", "config.json"), recursive=True)
        
        synced_count = 0
        for filepath in config_files:
            try:
                with open(filepath, 'r') as f:
                    data = json.load(f)
                
                # L'ID de session devient le nom du dossier parent 
                session_id = os.path.basename(os.path.dirname(filepath))
                acc = data.get("model", {}).get("test_multiclass_accuracy", {}).get("global", {}).get("avg_balanced_accuracy", 0)
                conf_matrix = data.get("output", {}).get("confusion_matrix_test", None)
                
                session, created = TrainingSession.objects.get_or_create(
                    session_id=session_id,
                    defaults={
                        'model_type': data.get("model", {}).get("type", "unknown"),
                        'epochs': data.get("model", {}).get("epochs", 0),
                        'learning_rate': data.get("model", {}).get("alpha", 0.0),
                        'accuracy': acc,
                        'confusion_matrix_filename': conf_matrix,
                    }
                )
                if created: synced_count += 1
            except Exception as e:
                print(f"Erreur lecture JSON: {e}")
        return synced_count
