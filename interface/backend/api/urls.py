from django.urls import path
from .views import predict_view, get_trained_models, get_model_metrics

urlpatterns = [
    path('predict/', predict_view, name='predict'),
    path('models/', get_trained_models, name='get_models'),
    path('models/<str:session_id>/metrics/', get_model_metrics, name='get_metrics'),
]