from django.db import models

class EngineType(models.TextChoices):
    GASOLINE = 'GASOLINE', 'Бензиновый'
    DIESEL = 'DIESEL', 'Дизельный'
    ELECTRIC = 'ELECTRIC', 'Электрический'
    HYBRID = 'HYBRID', 'Гибридный'
    HYDROGEN = 'HYDROGEN', 'Водородный'