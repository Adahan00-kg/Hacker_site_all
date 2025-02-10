from django.db.migrations.serializer import Serializer
from rest_framework import serializers
from .models import *


class CategorySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryLaptop
        fields = ['id', 'category_name']


class BrandLaptopSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandLaptop
        fields = ['id', 'brand_name']


class PhotoSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoLaptop
        fields =['id', 'img','color']


class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = ['id', 'characteristic_title','characteristic_description']


class LaptopListForBrandSerializer(serializers.ModelSerializer):
    photo_laptop = PhotoSimpleSerializer(many=True)
    category = CategorySimpleSerializer()

    class Meta:
        model = Laptop
        fields = ['id', 'laptop_name','description','price',
                  'brand','laptop_discount','photo_laptop','category']



class LaptopListForCategorySerializer(serializers.ModelSerializer):
    photo_laptop = PhotoSimpleSerializer(many=True)
    brand = BrandLaptopSimpleSerializer()
    class Meta:
        model = Laptop
        fields = ['id', 'laptop_name','description','price',
                  'brand','laptop_discount','photo_laptop']



class LaptopListSerializer(serializers.ModelSerializer):
    photo_laptop = PhotoSimpleSerializer(many=True)
    category = CategorySimpleSerializer()
    brand = BrandLaptopSimpleSerializer()
    class Meta:
        model = Laptop
        fields = ['id', 'laptop_name','description','price',
                  'category','brand','laptop_discount','photo_laptop']


class CategoryListSerializer(serializers.ModelSerializer):
    category_laptop = LaptopListForCategorySerializer(many=True)
    class Meta:
        model = CategoryLaptop
        fields = ['id', 'category_name','category_laptop']


class BrandListSerializer(serializers.ModelSerializer):
    brand_laptop = LaptopListForBrandSerializer(many=True)
    class Meta:
        model = BrandLaptop
        fields = ['id', 'brand_name','brand_laptop']


class LaptopDetailSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format('%d - %m - %Y %H:%M'))
    category = CategorySimpleSerializer()
    brand = BrandLaptopSimpleSerializer()
    characteristic_laptop = CharacteristicSerializer(many=True)
    photo_laptop = PhotoSimpleSerializer(many=True)
    class Meta:
        model = Laptop
        fields = ['id', 'laptop_name','description','price','laptop_discount',
                  'created_date','category','brand',
                  'characteristic_laptop','photo_laptop']
