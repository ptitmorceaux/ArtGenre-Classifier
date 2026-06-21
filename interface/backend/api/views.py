from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services import ArtClassifierService

def ping_view(request):
    return JsonResponse({'status': 'success', 'message': 'Pong !'})

@csrf_exempt # Désactive la vérification CSRF pour faciliter les tests depuis Vue.js
def predict_view(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Méthode non autorisée. Utilisez POST.'}, status=405)
        
    model_type = request.POST.get('model', 'mlp')
    image_file = request.FILES.get('image')
    
    if not image_file:
        return JsonResponse({'error': 'Aucune image fournie.'}, status=400)
        
    try:
        # On délègue tout le travail complexe au Service
        result = ArtClassifierService.predict(model_type, image_file)
        return JsonResponse({'status': 'success', 'data': result})
        
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)