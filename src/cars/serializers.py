from rest_framework import serializers
from .models import Car_Brand

class CarBrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car_Brand
        fields = ['id', 'name']