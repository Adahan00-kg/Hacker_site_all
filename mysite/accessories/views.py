from rest_framework import views, generics

from .serializers import *


class AccessoriesListView(generics.ListAPIView):
    queryset = Accessories.objects.all()
    serializer_class = AccessoriesSerializer


class ShortAccessListView(generics.ListAPIView):
    queryset = Accessories.objects.all()
    serializer_class = ShortAccessSerializer


class AccessCreateView(generics.CreateAPIView):
    queryset = Accessories.objects.all()
    serializer_class = AccessoriesSerializer


class AccessoriesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Accessories.objects.all()
    serializer_class = AccessoriesSerializer

