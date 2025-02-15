from django.urls import path, include
from .views import *

urlpatterns = [
    path('userprofile/<int:pk>/', UserProfileViewC.as_view(), name='userprofile-detail'),
    path('userprofile/', UserProfileViewC.as_view(), name='userprofile-detail'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


    path('cart_detail/<int:pk>/', CartDetailView.as_view(), name='detail_cart-list'),
    path('cart_list', CartListView.as_view(), name='cart-list'),
    
    path('cart_item/create/',CartItemCreateAPIView.as_view(),name = 'cart_item_create'),

    path('cart_item/<int:pk>/',CartItemUpdateDeleteAPIView.as_view(),name = 'cart_item_update'),

]



