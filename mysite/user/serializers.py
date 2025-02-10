from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'phone_number', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}



class CartItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'accessories', 'laptops', 'quantity', 'created_date']



class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemsSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'cart_items']


