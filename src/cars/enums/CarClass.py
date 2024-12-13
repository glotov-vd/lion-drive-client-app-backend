from django.db import models

class CarClass(models.TextChoices):
    SUV = 'SUV', 'Внедорожник'
    SPORTS = 'SPORTS', 'Спорткар'
    PREMIUM = 'PREMIUM', 'Премиум'
    BUSINESS = 'BUSINESS', 'Бизнес'
    MINIVAN = 'MINIVAN', 'Минивэн'
    COMFORT = 'COMFORT', 'Комфорт'
    ELECTRIC_CAR = 'ELECTRIC_CAR', 'Электромобиль'
    CONVERTIBLE = 'CONVERTIBLE', 'Кабриолет'