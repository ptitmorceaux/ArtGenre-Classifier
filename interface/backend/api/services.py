import os
import io
import glob
import base64
import json
import numpy as np

from PIL import Image
import matplotlib
import matplotlib.pyplot as plt

from engine.interop.storage import Storage

matplotlib.use('Agg')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

class ArtClassifierService:

    @staticmethod
    def process_image(image_file, config_data):
        resolution = 64
        channels = 3
        if "32x32" in str(config_data.get("dataset", {})):
            resolution = 32
            channels = 1
        mode = 'L' if channels == 1 else 'RGB'
        img = Image.open(image_file).convert(mode)
        
        resample = getattr(Image, "Resampling", Image).LANCZOS
        img = img.resize((resolution, resolution), resample)
        
        img_array = np.array(img).flatten().astype(np.float32)
        return img_array.tolist()

    @staticmethod
    def generate_matplotlib_chart(predictions, title):
        plt.figure(figsize=(7, 4))
        categories = list(predictions.keys())
        scores = list(predictions.values())
        colors = ['#2ecc71' if s > 0 else '#e74c3c' for s in scores]
        plt.bar(categories, scores, color=colors)
        plt.axhline(0, color='black', linewidth=1)
        plt.title(title)
        plt.ylabel("Score")
        plt.tight_layout()
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        image_base64 = base64.b64encode(buf.read()).decode('utf-8')
        plt.close()
        return image_base64

    @staticmethod
    def predict(session_id, image_file):
        output_dir = os.path.join(BASE_DIR, "engine", "core", "output")
        config_paths = glob.glob(os.path.join(output_dir, "**", session_id, "config.json"), recursive=True)
        
        if not config_paths:
            return {'error': f"Configuration introuvable pour la session {session_id}."}
            
        config_file_path = config_paths[0]
        session_dir = os.path.dirname(config_file_path)
        
        with open(config_file_path, 'r') as f:
            config_data = json.load(f)
            
        model_type = config_data.get("model", {}).get("type", "unknown")
        saved_models = config_data.get("model", {}).get("saved_models", {})
        
        is_classification = (model_type in ["mlp", "mlp_multiclass"])
        
        input_data = ArtClassifierService.process_image(image_file, config_data)
        input_size = len(input_data)
        predictions = {}
        
        models_dir = os.path.join(session_dir, "models")
        
        if model_type == "mlp_multiclass":
            # -- LOGIQUE MULTICLASSE NATIVE --
            if not saved_models:
                return {'error': "Aucun modèle sauvegardé trouvé dans la configuration."}
                
            # Il n'y a qu'un seul modèle pour toutes les catégories
            rel_model_path = list(saved_models.values())[0]
            normalized_path = rel_model_path.replace('\\', '/')
            model_filename = os.path.basename(normalized_path)
            model_path = os.path.join(models_dir, model_filename)
            
            if not os.path.exists(model_path):
                return {'error': f"Fichier .bin introuvable: {model_path}"}
                
            model, scaler = Storage["load"](model_path)
            normalized_data = scaler.transform(input_data)
            
            # raw_pred contiendra une liste des scores pour chaque neurone de sortie
            raw_pred = model.predict(normalized_data, is_classification=is_classification)
            
            # On récupère l'ordre exact des catégories tel que défini lors de l'entraînement
            expected_categories = list(config_data.get("dataset", {}).get("categories", {}).get("train", {}).keys())
            
            # On associe chaque score à la catégorie correspondante
            for i, category in enumerate(expected_categories):
                if i < len(raw_pred):
                    predictions[category] = float(raw_pred[i])
                else:
                    predictions[category] = 0.0
                    
            if hasattr(model, '_free'):
                model._free()
            elif hasattr(model, 'close'):
                model.close()
                
        else:
            # -- LOGIQUE ONE-VS-ALL EXISTANTE (linear, mlp, rbf) --
            for category, rel_model_path in saved_models.items():
                normalized_path = rel_model_path.replace('\\', '/')
                model_filename = os.path.basename(normalized_path)
                model_path = os.path.join(models_dir, model_filename)
                
                if not os.path.exists(model_path):
                    return {'error': f"Fichier .bin introuvable: {model_path}"}
                    
                model, scaler = Storage["load"](model_path)
                normalized_data = scaler.transform(input_data)
                
                raw_pred = model.predict(normalized_data, is_classification=is_classification)
                
                if isinstance(raw_pred, list):
                    predictions[category] = float(raw_pred[0])
                else:
                    predictions[category] = float(raw_pred)
                    
                if hasattr(model, '_free'):
                    model._free()
                elif hasattr(model, 'close'):
                    model.close()
                    
        best_category = max(predictions, key=predictions.get)
        chart_base64 = ArtClassifierService.generate_matplotlib_chart(
            predictions, f"Cheminement de décision - {model_type.upper()}"
        )
        
        return {
            'model_used': f"Modèle {model_type.upper()} (C)",
            'best_category': best_category,
            'raw_prediction': predictions,
            'chart_base64': chart_base64,
            'input_size': input_size
        }
