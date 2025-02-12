from rest_framework import serializers
from .models import *



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryAccessories
        fields = ['id', 'category']

class BrandAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandAccessories
        fields = ['id', 'brand']

class AIMGSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessIMG
        fields = ['id', 'img', 'color']

class PASerializer(serializers.ModelSerializer):
    class Meta:
        model = ParameterAccess
        fields = ['id', 'parameter', 'value_parameter']


class AccessoriesDetailSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format('%d - %m - %Y %H:%M'))
    img_accessories = AIMGSerializer(many=True)
    accessories = PASerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    brand =  BrandAccessSerializer(read_only=True)
    class Meta:
        model = Accessories
        fields = ['id', 'name', 'description', 'price', 'available', 'img_accessories', 'accessories', 'category', 'brand', 'created_date']

class AccessoriesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessories
        fields = ['id', 'name', 'description', 'price', 'available', 'img_accessories', 'accessories', 'category', 'brand']

class ShortAccessSerializer(serializers.ModelSerializer):

    class Meta:
        model = Accessories
        fields = ['id', 'name', 'description', 'price', 'available']


class CategoryAccessSerializer(serializers.ModelSerializer):
    category_access = ShortAccessSerializer(many=True,read_only=True)
    class Meta:
        model = CategoryAccessories
        fields = ['id', 'category','category_access']


class BrandAccessListSerializer(serializers.ModelSerializer):
    brand_access = ShortAccessSerializer(many=True,read_only=True)
    class Meta:
        model = BrandAccessories
        fields = ['id', 'brand', 'brand_access']


class AccessSimilarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Accessories
        fields = ['id', 'name', 'description', 'price', 'available']