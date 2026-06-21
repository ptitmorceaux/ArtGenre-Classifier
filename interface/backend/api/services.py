import os
from PIL import Image
from django.conf import settings
from engine.interop.mlp import MLP
# from engine.interop.linearModel import LinearModel

class ArtClassifierService:
    @staticmethod
    def process_image(image_file, target_size=(64, 64)):
        """
        Ouvre, redimensionne et normalise l'image reçue par l'API.
        Renvoie une liste 1D de floats [0.0, 1.0] prête pour le C.
        """
        img = Image.open(image_file).convert('RGB')
        img = img.resize(target_size)
        
        # Aplatissement et normalisation
        flat_data = [pixel_val / 255.0 for pixel in img.getdata() for pixel_val in pixel]
        return flat_data

    @classmethod
    def predict(cls, model_type, image_file):
        """
        Gère la prédiction selon le modèle choisi.
        """
        input_data = cls.process_image(image_file, target_size=(64, 64))
        input_size = len(input_data)

        if model_type == 'mlp':
            model = MLP([input_size, 128, 3]) # Exemple avec 3 classes de sortie
            prediction = model.predict(input_data, is_classification=True)
            model.close() # Libération de la mémoire en C
            
            return {
                'model_used': 'Perceptron Multi-Couches (C)',
                'raw_prediction': prediction,
            }
        elif model_type == 'linear':
            return {'error': "Le modèle linéaire n'est pas encore branché."}
        else:
            raise ValueError("Modèle inconnu.")