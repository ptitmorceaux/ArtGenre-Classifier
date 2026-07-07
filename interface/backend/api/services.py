from PIL import Image

from engine.interop.mlp import MLP
# from engine.interop.linearModel import LinearModel

class ArtClassifierService:
    @staticmethod
    def process_image(image_file):
        img = Image.open(image_file).convert('RGB')
        img = img.resize((32, 32))
        flat_data = [pixel_val / 255.0 for pixel in img.getdata() for pixel_val in pixel]
        return flat_data

    @staticmethod
    def predict(model_type, image_file):
        input_data = ArtClassifierService.process_image(image_file)
        input_size = len(input_data)

        if model_type == 'mlp':
            model = MLP([input_size, 128, 3])
            
            # --- LA PRÉDICTION  (MLP) ---
            prediction = model.predict(input_data, is_classification=True)
            model.close()
            
            return {
                'model_used': 'Perceptron Multi-Couches (C)',
                'raw_prediction': prediction,
                'input_size': input_size
            }
        elif model_type == 'linear':
            # --- LA PRÉDICTION  (Modèle Linéaire) ---
            # prediction = LinearModel.predict(input_data, is_classification=True)
            
            return {
                'model_used': 'Modèle Linéaire (C)',
                'raw_placeholder': input_data,
                'input_size': input_size
            }
        else:
            raise ValueError("Modèle inconnu.")