from rest_framework import serializers
from .models import *
from laptop.serializer import laptopForCartItemSerializer,LaptopImgSerializer
from accessories.serializers import ShortAccessSerializer

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'phone_number', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}







class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)



class CartItemCreateSerializer(serializers.ModelSerializer):
    laptops = laptopForCartItemSerializer(read_only=True)
    laptop_id = serializers.PrimaryKeyRelatedField(queryset=Laptop.objects.all(),write_only=True,source='laptops')
    laptop_img = LaptopImgSerializer(read_only=True)
    img_id = serializers.PrimaryKeyRelatedField(queryset=PhotoLaptop.objects.all(),write_only=True,source='laptop_img')
    accessories = ShortAccessSerializer(read_only=True)
    accessories_id = serializers.PrimaryKeyRelatedField(queryset=Accessories.objects.all(),write_only=True,source='accessories')
    class Meta:
        model = CartItem
        fields = ['id','laptops','laptop_id','quantity','laptop_img','img_id','accessories','accessories_id']



class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemCreateSerializer(many=True)
    class Meta:
        model = Cart
        fields = ['id','user','cart_items']


