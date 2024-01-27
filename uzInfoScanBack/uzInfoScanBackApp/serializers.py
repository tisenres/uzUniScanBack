from rest_framework import serializers
from .models import Item, LombardModel


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class HelloWorldSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=255)


class LombardModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LombardModel
        fields = '__all__'

