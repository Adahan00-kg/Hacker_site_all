from django.urls import path
from .views import *



urlpatterns = [
    path('accessories_short/', ShortAccessListView.as_view(), name='short_a-list'),
    path('accessories_detail/<int:pk>/', AccessoriesDetailView.as_view(), name='access-detail'),
    path('accessories_create/', AccessCreateView.as_view(), name='access-create'),


]
