from rest_framework import views, generics

from .serializers import *



class ShortAccessListView(generics.ListAPIView):
    queryset = Accessories.objects.all()
    serializer_class = ShortAccessSerializer


class AccessCreateView(generics.CreateAPIView):
    queryset = Accessories.objects.all()
    serializer_class = AccessoriesCreateSerializer

class AccessSecondCreateView(generics.CreateAPIView):
    queryset = Accessories.objects.all()
    serializer_class = AccessoriesCreateSecondSerializer

class AccessThordCreateView(generics.CreateAPIView):
    queryset = Accessories.objects.all()
    serializer_class = AccessoriesThordCreateSerializer



class AccessoriesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Accessories.objects.all()
    serializer_class = AccessoriesDetailSerializer

class CategoryAccessView(generics.ListAPIView):
    queryset = CategoryAccessories.objects.all()
    serializer_class = CategoryAccessSerializer

class BrandAccessView(generics.ListAPIView):
    queryset = BrandAccessories.objects.all()
    serializer_class = BrandAccessListSerializer

class AccessSimilarListView(generics.ListAPIView):
    queryset = Accessories.objects.all()
    serializer_class = AccessSimilarSerializer