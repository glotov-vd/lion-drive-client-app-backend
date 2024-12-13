from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

import uuid

from .enums.CarClass import CarClass
from .enums.ColorType import ColorType
from .enums.EngineType import EngineType
from .enums.TransmissionType import TransmissionType


class Car_Brand(models.Model):
    """
    Модель, представляющая бренд автомобиля

    id: Уникальный идентификатор (UUID)
    name: Название бренда автомобиля
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(max_length=100, unique=True)


class Car_Model(models.Model):
    """
    Модель, описывающая точную модель автомобиля

    id: Уникальный идентификатор (UUID)
    name: Название модели
    brand_id: Бренд автомобиля
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(max_length=250)

    brand_id = models.ForeignKey(Car_Brand, on_delete=models.CASCADE)


class Car(models.Model):
    """
    Модель, представляющая автомобиль

    id: Уникальный идентификатор (UUID)
    brand_id: Бренд автомобиля
    model_id: Модель автомобиля
    car_class: Класс автомобиля
    engine_type: Тип двигателя
    engine_power: Мощность двигателя (в л.с.)
    engine_volume: Объем двигателя
    transmission_type: Тип коробки передач
    release_year: Год выпуска автомобиля
    color_type: Цвет автомобиля
    number_of_seats: Количесто сидений
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    brand_id = models.ForeignKey(Car_Brand, on_delete=models.CASCADE, null=True)

    model_id = models.ForeignKey(Car_Model, on_delete=models.CASCADE, null=True)

    car_class = models.CharField(
        max_length=15,
        choices=CarClass.choices,
        default=CarClass.COMFORT,
        verbose_name="Класс автомобиля"
    )

    engine_type = models.CharField(
        max_length=15,
        choices=EngineType.choices,
        default=EngineType.GASOLINE,
        verbose_name="Тип двигателя"
    )

    engine_power = models.PositiveIntegerField()

    engine_volume = models.PositiveIntegerField()

    transmission_type = models.CharField(
        max_length=20,
        choices=TransmissionType.choices,
        default=TransmissionType.AUTOMATIC,
        verbose_name="Тип коробки передач"
    )

    release_year = models.IntegerField()

    color_type = models.CharField(
        max_length=20,
        choices=ColorType.choices,
        default=ColorType.BLACK,
        verbose_name="Цвет автомобиля"
    )

    number_of_seats = models.PositiveIntegerField(
        default=5,
        validators=[
            MinValueValidator(2),
            MaxValueValidator(9)
        ],
        verbose_name="Количество сидений",
    )