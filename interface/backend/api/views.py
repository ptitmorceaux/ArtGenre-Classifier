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
                    acc = data.get("model", {}).get("test_multiclass_accuracy", {}).get("global", {}).get("avg_balanced_accuracy", 0)
                
                acc_pct = f"{acc * 100:.1f}%" if acc else "N/A"
                
                resolution = 32 if "32x32" in str(data.get("dataset", {})) else 64
                
                results.append({
                    "id": session_id,
                    "type": model_type,
                    "resolution": resolution,
                    "accuracy": acc or 0,
                    "label": f"Précision: {acc_pct} | Session: {session_id}",
                    "hyperparameters": {
                        "alpha": data.get("model", {}).get("alpha", "N/A"),
                        "epochs": data.get("model", {}).get("epochs", "N/A"),
                        "npl": str(data.get("model", {}).get("npl", "N/A")),
                        "normalization": data.get("dataset", {}).get("normalization_method", "N/A")
                    }
                })
            except Exception as e:
                continue
            
    results = sorted(results, key=lambda x: x["accuracy"], reverse=True)
    return Response({"status": "success", "models": results})

@api_view(['GET'])
def get_model_metrics(request, session_id):
    output_dir = os.path.join(BASE_DIR, "engine", "core", "output")
    session_dir = None

    for root, dirs, files in os.walk(output_dir):
        if os.path.basename(root) == session_id and "config.json" in files:
            session_dir = root
            break
    
    if not session_dir:
        return Response({"status": "error", "message": "Session introuvable"}, status=404)

    metrics_data = {}
    matrix_filename = "confusion_matrix_test.png"
    
    try:
        with open(os.path.join(session_dir, "config.json"), 'r') as f:
            config_data = json.load(f)
            # Récupération des TPR/TNR
            metrics_data = config_data.get("model", {}).get("test_multiclass_accuracy", {}).get("categories", {})
            # Correction du chemin Windows -> Linux
            raw_matrix_path = config_data.get("output", {}).get("confusion_matrix_test", "")
            if raw_matrix_path:
                matrix_filename = os.path.basename(raw_matrix_path.replace('\\', '/'))
    except Exception as e:
        print(f"Erreur de lecture des métriques: {e}")

    encoded_string = None
    full_path = os.path.join(session_dir, matrix_filename)
    if os.path.exists(full_path):
        with open(full_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            
    return Response({
        "status": "success",
        "session_id": session_id,
        "confusion_matrix": encoded_string,
        "metrics": metrics_data
    })

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