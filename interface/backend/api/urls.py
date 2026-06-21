from django.urls import path
from .views import predict_view, test

urlpatterns = [
    path('predict/', predict_view, name='predict'), 
    path("test/", test, name="test"),
]