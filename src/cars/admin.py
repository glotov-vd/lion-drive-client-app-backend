from django.contrib import admin
from .models import Car, Car_Brand, Car_Model

admin.site.register(Car)
admin.site.register(Car_Brand)
admin.site.register(Car_Model)