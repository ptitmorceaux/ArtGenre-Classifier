import os
from PIL import Image
from django.conf import settings
from engine.interop.mlp import MLP
from engine.interop.linearModel import LinearModel

class ArtClassifierService:
    """
    Service orchestrant le chargement des modèles C via l'interop Python
    et le traitement d'images via Pillow.
    """
    
    @staticmethod
    def process_image(image_file, target_size=(64, 64)):
        """
        Ouvre, redimensionne et normalise l'image reçue par l'API.
        Renvoie un tableau plat (1D) de floats prêt pour le modèle en C.
        """
        img = Image.open(image_file).convert('RGB')
        img = img.resize(target_size)
        
        # Transformation des pixels [0, 255] en floats normalisés [0.0, 1.0]
        flat_data = [pixel_val / 255.0 for pixel in img.getdata() for pixel_val in pixel]
        return flat_data

    @classmethod
    def predict(cls, model_type, image_file):
        """
        Prend en charge le type de modèle demandé, applique la transformation d'image
        et appelle la bibliothèque dynamique C.
        """
        # 1. Préparation des données de l'image
        # La taille cible doit être proportionnelle au nombre d'entrées du modèle (ex: 64x64x3 = 12288)
        input_data = cls.process_image(image_file, target_size=(64, 64))
        input_size = len(input_data)

        if model_type == 'mlp':
            # Exemple d'architecture : input_size -> Couche cachée (128) -> Output (3 classes d'art)
            # A terme, l'initialisation lira un fichier de poids sauvegardé dans settings.MODEL_WEIGHTS_DIR
            model = MLP([input_size, 128, 3])
            
            # Exemple théorique de chargement requis par le syllabus :
            # weights_path = os.path.join(settings.MODEL_WEIGHTS_DIR, 'mlp_art_genre.bin')
            # if os.path.exists(weights_path):
            #     model.load_weights(weights_path)

            raw_prediction = model.predict(input_data, is_classification=True)
            model.close() # Libération critique de la mémoire allouée en C
            
            return {
                'model': 'Multi-Layer Perceptron (C Impl)',
                'classes_probabilities': raw_prediction,
                'predicted_class_index': raw_prediction.index(max(raw_prediction))
            }
            
        elif model_type == 'linear':
            # Logique d'appel pour votre modèle linéaire en C
            return {'model': 'Linear Model', 'info': 'En attente d\'intégration'}
            
        else:
            raise ValueError(f"Le modèle '{model_type}' n'est pas pris en charge par le moteur.")