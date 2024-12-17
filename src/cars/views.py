from rest_framework.decorators import api_view
from rest_framework.response import Response

from cars.models import Car_Brand, Car
from cars.serializers import CarBrandSerializer, CarSerializer

@api_view(['GET'])
def get_all_brands(request):
    """
    Представление для получения списка всех брендов автомобилей
    """

    if request.method == 'GET':
        brands = Car_Brand.objects.all()
        serializer = CarBrandSerializer(brands, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_all_cars(request):
    """
    Представление для получения списка всех автомобилей
    """
    
    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_brand_cars(request, brand_name):
    """
    Представление для получения списка всех автомобилей заданного бренда
    """
    
    if request.method == 'GET':
        cars = Car.objects.filter()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)