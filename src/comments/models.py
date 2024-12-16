from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

import uuid
from src.cars.models import Car


class Comments(models.Model):
    """
    Модель, представляющаяя комментарии
    
    id: Уникальный идентификатор (UUID)
    car_id: Уникальный идентификатор автомобиля, к которому относится комментарий
    comment: Текст комментария
    rating_score: Рейтинг комментария
    comment_date: Дата написания комментария
    client_name: Имя клиента, оставившего комментарий
    """
    
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    
    comment = models.TextField(null=False)
    
    rating_score = models.models.PositiveIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ],
        verbose_name="Рейтинг",
    )
    
    comment_date = models.DateField(auto_now_add=True, null=False)
    
    client_name = models.TextField(null=False)
