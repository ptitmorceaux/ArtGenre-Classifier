from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services import ArtClassifierService

@csrf_exempt
def classify_art_view(request):
    """
    Point d'accès API pour analyser une œuvre d'art via les modèles C.
    Attend un paramètre POST 'model' et un fichier 'image'.
    """
    if request.method != 'POST':
        return JsonResponse({'error': 'Méthode non autorisée. Utilisez POST.'}, status=405)
        
    model_type = request.POST.get('model', 'mlp')
    image_file = request.FILES.get('image')
    
    if not image_file:
        return JsonResponse({'error': 'Aucun fichier image trouvé dans la requête.'}, status=400)
        
    try:
        # Délégation complète de la logique métier au service dédié
        result = ArtClassifierService.predict(model_type, image_file)
        return JsonResponse({'status': 'success', 'data': result})
        
    except ValueError as val_err:
        return JsonResponse({'status': 'error', 'message': str(val_err)}, status=400)
    except Exception as e:
        # Optionnel : logguer l'erreur ici de manière centralisée
        return JsonResponse({'status': 'error', 'message': f"Erreur interne du serveur: {str(e)}"}, status=500)