# interface/backend/api/views.py
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from engine.interop.mlp import MLP 

def ping_view(request):
    return JsonResponse({'status': 'success', 'message': 'Pong !'})

@csrf_exempt
def predict_view(request):
    if request.method == 'POST':
        try:
            # Simulation d'une image aplatie en attendant l'intégration PIL
            dummy_pixels = [0.5, 0.1, -0.2, 0.9] 
            layers = [4, 8, 3]
            model = MLP(layers) 
            
            prediction = model.predict(dummy_pixels, is_classification=True)
            
            return JsonResponse({
                "status": "success",
                "prediction": prediction
            })
            
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
            
    return JsonResponse({"status": "error", "message": "Method not allowed"}, status=405)