import os
import json
import glob
import base64

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TrainingSession
from engine.core.config import CONFIG

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

@api_view(['GET'])
def get_trained_models(request):
    """Synchronise la BDD avec les JSON, puis renvoie la liste triée."""
    metrics_base_dir = os.path.join(BASE_DIR, CONFIG["output"]["outdir"], "metrics")
    
    # SYNCHRONISATION
    if os.path.exists(metrics_base_dir):
        for session_folder in os.listdir(metrics_base_dir):
            json_path = os.path.join(metrics_base_dir, session_folder, "metadata.json")
            if os.path.isfile(json_path):
                with open(json_path, 'r') as f:
                    data = json.load(f)
                    TrainingSession.objects.get_or_create(
                        session_id=data['session_id'],
                        defaults={
                            'model_type': data['model_type'],
                            'epochs': data['hyperparameters'].get('epochs', 0),
                            'learning_rate': data['hyperparameters'].get('alpha', 0.0),
                            'accuracy': data['metrics'].get('accuracy', 0)
                        }
                    )

    # RENVOIE LA LISTE TRIÉE PAR ACCURACY
    models = TrainingSession.objects.all().order_by('-accuracy')
    results = []
    for m in models:
        acc_pct = f"{m.accuracy * 100:.1f}%" if m.accuracy else "N/A"
        results.append({
            "id": m.session_id,
            "type": m.model_type,
            "label": f"{m.model_type.upper()} | Acc: {acc_pct} | {m.session_id}"
        })
        
    return Response({"status": "success", "models": results})

@api_view(['GET'])
def get_model_metrics(request, session_id):
    """Renvoie les 3 images (Loss, Accuracy, Matrice) en Base64 pour le frontend."""
    metrics_dir = os.path.join(BASE_DIR, CONFIG["output"]["outdir"], "metrics", session_id)
    
    def image_to_base64(filename):
        path = os.path.join(metrics_dir, filename)
        if os.path.exists(path):
            with open(path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')
        return None

    return Response({
        "status": "success",
        "session_id": session_id,
        "loss_curve": image_to_base64("loss_curve.png"),
        "accuracy_curve": image_to_base64("accuracy_curve.png"),
        "confusion_matrix": image_to_base64("confusion_matrix.png")
    })
