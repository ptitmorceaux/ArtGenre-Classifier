from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from PIL import Image
import os
import base64

from .services import ArtClassifierService, ModelSyncService
from .models import TrainingSession

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
MAX_IMAGE_SIZE = 5 * 1024 * 1024 

@api_view(['GET'])
def get_trained_models(request):
    """Synchronise la BDD avec les config.json, puis renvoie la liste triée."""
    ModelSyncService.sync_models_to_db()
    
    models = TrainingSession.objects.all().order_by('-accuracy')
    results = []
    for m in models:
        acc_pct = f"{m.accuracy * 100:.1f}%" if m.accuracy else "N/A"
        results.append({
            "id": m.session_id,
            "type": m.model_type,
            "label": f"{m.model_type.upper()} | Précision: {acc_pct} | Session: {m.session_id}"
        })
    return Response({"status": "success", "models": results})

@api_view(['GET'])
def get_model_metrics(request, session_id):
    """Renvoie la matrice de confusion en Base64."""
    try:
        session = TrainingSession.objects.get(session_id=session_id)
    except TrainingSession.DoesNotExist:
        return Response({"status": "error", "message": "Session introuvable"}, status=404)
        
    def image_to_base64(filepath):
        if not filepath: return None
        path = os.path.join(BASE_DIR, filepath) # Chemin relatif présent dans config.json
        if os.path.exists(path):
            with open(path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')
        return None

    return Response({
        "status": "success",
        "session_id": session_id,
        "confusion_matrix": image_to_base64(session.confusion_matrix_filename)
    })

@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser])
def predict_view(request):
    if request.method == 'GET':
        return Response({"status": "Ready"})

    try:
        image_file = request.FILES.get('image')
        session_id = request.data.get('session_id') # ON ATTRAPE LA SESSION

        if not image_file: return Response({"status": "error", "message": "Aucune image."}, status=400)
        if not session_id: return Response({"status": "error", "message": "Aucune session sélectionnée."}, status=400)

        # On appelle le service avec la session précise
        prediction_result = ArtClassifierService.predict(session_id, image_file)

        if 'error' in prediction_result:
            return Response({"status": "error", "message": prediction_result['error']}, status=400)

        return Response({"status": "success", "data": prediction_result})
    except Exception as e:
        return Response({"status": "error", "message": f"Erreur serveur: {str(e)}"}, status=500)