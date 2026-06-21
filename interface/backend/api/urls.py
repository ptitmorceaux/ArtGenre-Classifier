from django.urls import path
from .views import ping_view, predict_view

urlpatterns = [
    path('ping/', ping_view, name='ping'),
    path('predict/', predict_view, name='predict'), # La nouvelle route !
]