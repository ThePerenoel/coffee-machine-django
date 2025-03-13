from rest_framework import serializers

from api.models import DrinkOrder

class DrinkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrinkOrder
        fields = ['id', 'drink_type', 'number_of_sugars', 'is_extra_hot']

class DrinkOrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrinkOrder
        fields = ['drink_type', 'number_of_sugars', 'is_extra_hot']
