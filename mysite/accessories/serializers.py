from rest_framework import serializers
from .models import *



class AIMGSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessIMG
        fields = ['id', 'img']

class PASerializer(serializers.ModelSerializer):
    class Meta:
        model = ParameterAccess
        fields = ['id', 'parameter', 'value_parameter']


class AccessoriesSerializer(serializers.ModelSerializer):
    img_accessories = AIMGSerializer(many=True, read_only=True)
    accessories = PASerializer(many=True, read_only=True)
    class Meta:
        model = Accessories
        fields = ['id', 'name', 'description', 'price', 'available', 'img_accessories', 'accessories']


class ShortAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessories
        fields = ['id', 'name', 'description', 'price', 'available']
