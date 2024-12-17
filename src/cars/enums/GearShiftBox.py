from django.db import models

class CarClass(models.TextChoices):
    MECH = 'MECH', 'Механическая'
    AUTO = 'AUTO', 'Автоматическая'
    ROBO = 'ROBO', 'Роботизированная'
    VARI = 'VARI', 'Внедорожник'