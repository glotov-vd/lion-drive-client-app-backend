from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Tarifs
from .serializers import TarifsSerializer

@api_view(['GET'])
def get_tarifs(request, car_id):
    """
    Представление для получения списка тарифов на автомобиль
    """

    if request.method == 'GET':
        tarifs = Tarifs.objects.get(car_id=car_id)
        serializer = TarifsSerializer(tarifs)
        return Response(serializer.data)
