from django.urls import path

from cars import views

urlpatterns = [
    path('brands/', views.get_all_brands, name='car_brands_list'),
]