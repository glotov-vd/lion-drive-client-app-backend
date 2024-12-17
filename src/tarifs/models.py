from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from cars.models import Car

import uuid


class Prices(models.Model):
    """
    Модель, представляющая цену за конкретный тариф
    
    id: Уникальный идентификатор (UUID)
    price: назначенная цена
    discount_percents: процент скидки
    is_individual: цена задана или назначается индивидуально
    """
    
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    price = models.PositiveIntegerField()
    
    discount_percents = models.PositiveIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    
    is_individual = models.BooleanField(default=False)


class Tarifs(models.Model):
    """
    Модель, представляющая тарифы аренды
    
    id: Уникальный идентификатор (UUID)
    car_id: идентификатор автомобиля, к которому относятся тарифы
    days_1_1_id: идентификатор объекта класса Prices, отвечающий за цену за аренду на 1 день
    days_2_3_id: идентификатор объекта класса Prices, отвечающий за цену за аренду на 2-3 дня
    days_4_6_id: идентификатор объекта класса Prices, отвечающий за цену за аренду на 4-6 дней
    days_7_14_id: идентификатор объекта класса Prices, отвечающий за цену за аренду на 7-14 дней
    days_15_21_id: идентификатор объекта класса Prices, отвечающий за цену за аренду на 15-21 день
    days_more_21_id: идентификатор объекта класса Prices, отвечающий за цену за аренду на больше, чем 21 день
    """
    
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    
    days_1_1_id = models.ForeignKey(Prices, on_delete=models.CASCADE)
    
    days_2_3_id = models.ForeignKey(Prices, on_delete=models.CASCADE)
    
    days_4_6_id = models.ForeignKey(Prices, on_delete=models.CASCADE)
    
    days_7_14_id = models.ForeignKey(Prices, on_delete=models.CASCADE)
    
    days_15_21_id = models.ForeignKey(Prices, on_delete=models.CASCADE)
    
    days_more_21_id = models.ForeignKey(Prices, on_delete=models.CASCADE)
