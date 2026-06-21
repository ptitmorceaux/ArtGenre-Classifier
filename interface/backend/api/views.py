# interface/backend/api/views.py
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response


from engine.interop.mlp import MLP 

@api_view(['POST'])
def predict_view(request):
    """Predict the output based on the input image data.
    Returns
    -------
    Response
        A JSON response containing the prediction result.
    """
    try:
        # TODO: remplacer par le traitement réel de l'image
        dummy_pixels = [0.5, 0.1, -0.2, 0.9]

        layers = [4, 8, 3]
        model = MLP(layers)

        prediction = model.predict(
            dummy_pixels,
            is_classification=True
        )

        return Response({
            "status": "success",
            "prediction": prediction
        })

    except Exception as e:
        return Response({
            "status": "error",
            "message": str(e)
        }, status=500)


@api_view(['GET'])
def test(request):
    """A simple test endpoint to verify that the API is working.
    Returns
    -------
    Response
        A JSON response indicating that the test endpoint is working.
    """
    return Response({
        "status": "success",
        "message": "Test endpoint is working!"
    })