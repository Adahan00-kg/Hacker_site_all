from rest_framework.viewsets import generics
from .models import *
from .serializer import *


class LaptopListAPIView(generics.ListAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopListSerializer


class LaptopDetailAPIView(generics.RetrieveAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopDetailSerializer


class CategoryLaptopListAPIView(generics.ListAPIView):
    queryset = CategoryLaptop.objects.all()
    serializer_class = CategoryListSerializer


class BrandListAPIView(generics.ListAPIView):
    queryset = BrandLaptop.objects.all()
    serializer_class = BrandListSerializer



