from rest_framework.decorators import api_view
from rest_framework.response import Response

from cars.models import Car_Brand
from cars.serializers import CarBrandSerializer

@api_view(['GET'])
def get_all_brands(request):
    """
    Представление для получения списка всех брендов автомобилей
    """

    if request.method == 'GET':
        brands = Car_Brand.objects.all()
        serializer = CarBrandSerializer(brands, many=True)
        return Response(serializer.data)
