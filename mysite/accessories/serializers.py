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

class AIMGCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessIMG
        fields = ['id', 'img', 'color']

class PACreateSerializer(serializers.ModelSerializer):
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
    img_accessories = AIMGSerializer(many=True)
    accessories = PASerializer(many=True)
    class Meta:
        model = Accessories
        fields = ['id', 'category', 'brand', 'name', 'description', 'price', 'available', 'accessor_discount', 'created_date', 'img_accessories', 'accessories']


class AccessoriesCreateSecondSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessories
        fields = ['id', 'category', 'brand', 'name', 'description', 'price', 'available', 'accessor_discount', 'created_date', 'img_accessories', 'accessories']


class AccessoriesThordCreateSerializer(serializers.ModelSerializer):
    # Здесь many=True, т.к. аксессуар может иметь несколько изображений.
    img_accessories = AIMGSerializer(many=True)

    class Meta:
        model = Accessories
        fields = [
            'id', 'category', 'brand', 'name', 'description', 'price',
            'available', 'accessor_discount', 'created_date', 'img_accessories'
        ]

    def create(self, validated_data):
        # Извлекаем данные для изображений
        images_data = validated_data.pop('img_accessories', [])
        # Создаем аксессуар
        accessory = Accessories.objects.create(**validated_data)
        # Создаем связанные изображения
        for image_data in images_data:
            AccessIMG.objects.create(accessories=accessory, **image_data)
        return accessory

class ShortAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessories
        fields = ['id', 'name', 'description', 'price', 'available']


class AccessForCategorySerializer(serializers.ModelSerializer):
    img_accessories = AIMGSerializer(many=True)
    class Meta:
        model = Accessories
        fields = ['id', 'name', 'description', 'price', 'available', 'img_accessories']


class CategoryAccessSerializer(serializers.ModelSerializer):
    category_access = AccessForCategorySerializer(many=True,read_only=True)
    class Meta:
        model = CategoryAccessories
        fields = ['id', 'category','category_access']


class BrandAccessListSerializer(serializers.ModelSerializer):
    brand_access = AccessForCategorySerializer(many=True,read_only=True)
    class Meta:
        model = BrandAccessories
        fields = ['id', 'brand', 'brand_access']


class AccessSimilarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Accessories
        fields = ['id', 'name', 'description', 'price', 'available']