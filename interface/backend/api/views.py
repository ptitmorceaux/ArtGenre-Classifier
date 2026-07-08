from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from PIL import Image

from .services import ArtClassifierService 

MAX_IMAGE_SIZE = 5 * 1024 * 1024 

@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser])
def predict_view(request):
    """Predict the output based on the input image data."""


    if request.method == 'GET':
        return Response({
            "status": "Ready",
            "message": "Interface de l'API de Classification. L'API est prête à recevoir une requête POST avec une 'image' et le paramètre 'model'."
        })
    try:
        image_file = request.FILES.get('image')
        model_type = request.data.get('model')

        if not image_file:
            return Response({"status": "error", "message": "Aucune image fournie."}, status=400)
            
        if not model_type:
            return Response({"status": "error", "message": "Aucun modèle sélectionné."}, status=400)

        if image_file.size > MAX_IMAGE_SIZE:
            return Response({"status": "error", "message": f"Taille maximum : {MAX_IMAGE_SIZE / (1024*1024)} Mo."}, status=400)

        try:
            with Image.open(image_file) as img:
                img.verify()
        except Exception:
            return Response({"status": "error", "message": "Fichier corrompu ou fausse image."}, status=400)

        model_type = str(model_type).strip().lower()
        if model_type not in ["mlp", "linear"]:
            return Response({"status": "error", "message": "Modèle non supporté ('mlp' ou 'linear')."}, status=400)

        prediction_result = ArtClassifierService.predict(model_type, image_file)

        if 'error' in prediction_result:
            return Response({"status": "error", "message": prediction_result['error']}, status=400)

        return Response({
            "status": "success",
            "data": prediction_result
        })

    except Exception as e:
        return Response({
            "status": "error",
            "message": f"Erreur interne du serveur: {str(e)}"
        }, status=500)
    