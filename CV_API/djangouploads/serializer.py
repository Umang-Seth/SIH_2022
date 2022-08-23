from rest_framework import serializers
from .models import Drink, ImageInfo


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageInfo
        fields = ['id','image']