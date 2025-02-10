from django.urls import path, include
from .views import *

urlpatterns = [
    path('userprofile/<int:pk>/', UserProfileViewC.as_view(), name='userprofile-detail'),
    path('userprofile/', UserProfileViewC.as_view(), name='userprofile-detail'),

    path('cart_detail/<int:pk>/', CartDetailView.as_view(), name='detail_cart-list'),
    path('cart_list', CartListView.as_view(), name='cart-list'),

]



