# interface/backend/api/views.py
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from PIL import Image

# Import de votre service de classification existant
from .services import ArtClassifierService 

# Configuration du garde-fou pour la taille (ex: 5 Mo maximum)
MAX_IMAGE_SIZE = 5 * 1024 * 1024 

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def predict_view(request):
    """Predict the output based on the input image data."""
    try:
        # 1. Récupération de l'image et du modèle depuis la requête FormData
        image_file = request.FILES.get('image')
        model_type = request.data.get('model')

        # 2. Vérifications de base (présence des données)
        if not image_file:
            return Response({"status": "error", "message": "Aucune image fournie."}, status=400)
            
        if not model_type:
            return Response({"status": "error", "message": "Aucun modèle sélectionné."}, status=400)

        # 3. Garde-fou 1 : Limite de poids du fichier (évite la saturation de la mémoire)
        if image_file.size > MAX_IMAGE_SIZE:
            return Response({
                "status": "error", 
                "message": f"L'image est trop volumineuse. Taille maximum : {MAX_IMAGE_SIZE / (1024*1024)} Mo."
            }, status=400)

        # 4. Garde-fou 2 : Détection des "fausses" images (Vérification du format réel)
        try:
            # On tente d'ouvrir le fichier avec Pillow
            with Image.open(image_file) as img:
                # verify() inspecte les en-têtes internes du fichier pour confirmer le type réel
                img.verify()
                
                # Optionnel : Vous pouvez aussi restreindre strictement aux formats voulus (PNG, JPEG)
                if img.format not in ['PNG', 'JPEG', 'MPO']: # Note: MPO est souvent lié au JPEG
                    return Response({
                        "status": "error", 
                        "message": f"Format réel de l'image ({img.format}) non supporté. Seuls PNG et JPEG sont acceptés."
                    }, status=400)
        except Exception:
            # Si Pillow n'arrive pas à ouvrir ou vérifier le fichier, c'est une fausse image (ex: un .txt renommé en .png)
            return Response({
                "status": "error", 
                "message": "Le fichier envoyé est corrompu ou n'est pas une véritable image valide."
            }, status=400)

        # 5. Application du choix du modèle (.lower() et nettoyage)
        model_type = str(model_type).strip().lower()
        
        if model_type not in ["mlp", "linear"]:
            return Response({
                "status": "error", 
                "message": f"Modèle '{model_type}' non supporté. Veuillez choisir 'mlp' ou 'linear'."
            }, status=400)

        # 6. Appel du service de prédiction (l'image est maintenant sûre)
        prediction_result = ArtClassifierService.predict(model_type, image_file)

        if 'error' in prediction_result:
            return Response({
                "status": "error",
                "message": prediction_result['error']
            }, status=400)

        return Response({
            "status": "success",
            "data": prediction_result
        })

    except Exception as e:
        return Response({
            "status": "error",
            "message": f"Erreur interne du serveur: {str(e)}"
        }, status=500)
