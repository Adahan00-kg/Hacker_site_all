from django.urls import path, include
from .views import *

urlpatterns = [
    path('userprofile/<int:pk>/', UserProfileViewC.as_view(), name='userprofile-detail'),
    path('userprofile/', UserProfileViewC.as_view(), name='userprofile-detail'),

]