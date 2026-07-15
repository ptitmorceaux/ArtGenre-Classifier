from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
import os
import base64
import json

from .services import ArtClassifierService

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

@api_view(['GET'])
def get_trained_models(request):
    """Recherche infaillible de tous les config.json et extraction des hyperparamètres."""
    output_dir = os.path.join(BASE_DIR, "engine", "core", "output")
    results = []

    for root, dirs, files in os.walk(output_dir):
        if "config.json" in files:
            filepath = os.path.join(root, "config.json")
            try:
                with open(filepath, 'r') as f:
                    data = json.load(f)
                
                session_id = os.path.basename(root)
                model_type = data.get("model", {}).get("type", "unknown").lower()
                
                try:
                    acc = data["model"]["test_multiclass_accuracy"]["global"]["top1_accuracy"]
                except KeyError:
                    try:
                        acc = data["model"]["test_multiclass_accuracy"]["global"]["avg_balanced_accuracy"]
                    except KeyError:
                        acc = 0
                
                acc_pct = f"{acc * 100:.1f}%" if acc else "N/A"
                
                results.append({
                    "id": session_id,
                    "type": model_type,
                    "accuracy": acc or 0,
                    "label": f"Précision: {acc_pct} | {session_id}",
                    "hyperparameters": {
                        "alpha": data.get("model", {}).get("alpha", "N/A"),
                        "epochs": data.get("model", {}).get("epochs", "N/A"),
                        "npl": str(data.get("model", {}).get("npl", "N/A")),
                        "normalization": data.get("dataset", {}).get("normalization_method", "N/A")
                    }
                })
            except Exception as e:
                print(f"Erreur de lecture sur {filepath}: {e}")
                continue
            
    results = sorted(results, key=lambda x: x["accuracy"], reverse=True)
    return Response({"status": "success", "models": results})

@api_view(['GET'])
def get_model_metrics(request, session_id):
    """Récupère l'image de la matrice de confusion en Base64 de manière dynamique."""
    output_dir = os.path.join(BASE_DIR, "engine", "core", "output")
    matrix_path = None
    session_dir = None

    for root, dirs, files in os.walk(output_dir):
        if os.path.basename(root) == session_id and "config.json" in files:
            session_dir = root
            with open(os.path.join(root, "config.json"), 'r') as f:
                config_data = json.load(f)
                matrix_path = config_data.get("output", {}).get("confusion_matrix_test")
            break
    
    if not matrix_path or not session_dir:
        return Response({"status": "error", "message": "Matrice introuvable pour cette session"}, status=404)
    
    normalized_matrix_path = matrix_path.replace('\\', '/')
    matrix_filename = os.path.basename(normalized_matrix_path)
    full_path = os.path.join(session_dir, matrix_filename)
    
    if os.path.exists(full_path):
        with open(full_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            return Response({"status": "success", "confusion_matrix": encoded_string})
            
    return Response({"status": "error", "message": "Fichier image inexistant sur le disque"}, status=404)

@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, FormParser])
def predict_view(request):
    if request.method == 'GET':
        return Response({"status": "Ready"})

    try:
        image_file = request.FILES.get('image')
        session_id = request.data.get('session_id')

        if not image_file: return Response({"status": "error", "message": "Aucune image."}, status=400)
        if not session_id: return Response({"status": "error", "message": "Aucune session sélectionnée."}, status=400)

        prediction_result = ArtClassifierService.predict(session_id, image_file)

        if 'error' in prediction_result:
            return Response({"status": "error", "message": prediction_result['error']}, status=400)

        return Response({"status": "success", "data": prediction_result})
    except Exception as e:
        return Response({"status": "error", "message": f"Erreur serveur: {str(e)}"}, status=500)