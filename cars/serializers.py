from rest_framework import serializers
from cars.models import Car

class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class CarDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Car
        fields = '__all__'
