from rest_framework import serializers
from items.models import Food, Food_Choise

class FoodChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food_Choise
        fields = "__all__"

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"