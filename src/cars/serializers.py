from rest_framework import serializers
from .models import Car_Brand, Car, Car_Model

class CarBrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car_Brand
        fields = ['id', 'name']

class CarModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car_Model
        fields = ['id', 'name']


class CarSerializer(serializers.ModelSerializer):
    brand_id = CarBrandSerializer()
    model_id = CarModelSerializer()
    
    
    class Meta:
        model = Car
        fields = ['id', 'car_class', 'brand_id', 'engine_type', 'model_id', 'engine_power', 
                  'release_year', 'engine_volume', 'Transmission_type', 'color_type', 
                  'count_of_seats', 'gear_shift_box']