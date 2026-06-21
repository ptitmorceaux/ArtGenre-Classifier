from django.http import JsonResponse

def ping_view(request):
    return JsonResponse({
        'status': 'success', 
        'message': 'Pong ! La tuyauterie Django-Vue fonctionne à merveille.'
    })