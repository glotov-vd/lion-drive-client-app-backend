from django.db import models

class TransmissionType(models.TextChoices):
    MANUAL = 'MANUAL', 'Механическая'
    AUTOMATIC = 'AUTOMATIC', 'Автоматическая'
    SEMI_AUTOMATIC = 'SEMI_AUTOMATIC', 'Полуавтоматическая'
    CVT = 'CVT', 'Вариатор'
    DUAL_CLUTCH = 'DUAL_CLUTCH', 'Роботизированная (двойное сцепление)'
