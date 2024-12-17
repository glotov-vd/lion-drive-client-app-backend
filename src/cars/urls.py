from django.urls import path, re_path

from cars import views

urlpatterns = [
    re_path(r'^cars', views.get_all_cars),
    re_path(r'^brands/<str:brand_name>/cars', views.get_all_cars),
    re_path(r'^brands', views.get_all_brands, name='car_brands_list'),
]