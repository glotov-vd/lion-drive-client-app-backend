from django.urls import re_path

from cars import views

urlpatterns = [
    re_path(r'^cars/<uuid:car_id>/tarifs', views.get_all_brands),
]