from rest_framework import serializers
from .models import Tarifs, Prices

class PricesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Prices
        fields = ["price", "discount_percents", "is_individual"]

class TarifsSerializer(serializers.ModelSerializer):
    days_1_1_id = PricesSerializer()
    days_2_3_id = PricesSerializer()
    days_4_6_id = PricesSerializer()
    days_7_14_id = PricesSerializer()
    days_15_21_id = PricesSerializer()
    days_more_21_id = PricesSerializer()
    
    class Meta:
        model = Tarifs
        fields = ["car_id", "days_1_1_id", "days_2_3_id", "days_4_6_id", "days_7_14_id", "days_15_21_id", "days_more_21_id"]
