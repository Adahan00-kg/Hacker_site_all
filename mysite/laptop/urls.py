from django.urls import path
from .views import *


urlpatterns = [
    path('laptop_list/',LaptopListAPIView.as_view(),name = 'laptop_list'),
    path('laptop_detail/<int:pk>/',LaptopDetailAPIView.as_view(),name = 'laptop_detail'),
    path('laptop_category/',CategoryLaptopListAPIView.as_view(),name = 'laptop_category'),
    path('laptop_brand/',BrandListAPIView.as_view(),name = 'brand_laptop'),
    ]