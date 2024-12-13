from django.db import models

class ColorType(models.TextChoices):
    WHITE = 'WHITE', 'Белый'
    BLACK = 'BLACK', 'Чёрный'
    SILVER = 'SILVER', 'Серебристый'
    GREY = 'GREY', 'Серый'
    BLUE = 'BLUE', 'Синий'
    RED = 'RED', 'Красный'
    GREEN = 'GREEN', 'Зелёный'
    YELLOW = 'YELLOW', 'Жёлтый'
    ORANGE = 'ORANGE', 'Оранжевый'
    BROWN = 'BROWN', 'Коричневый'
    GOLD = 'GOLD', 'Золотой'
    PURPLE = 'PURPLE', 'Фиолетовый'