from rest_framework import  serializers

from car.models import Car, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name", "full_name"]
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name", "full_name"]
class CarSerializer(serializers.ModelSerializer):
    class Meat:
        model = Car
        fields = "__all__"
