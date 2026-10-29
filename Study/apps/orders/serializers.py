from rest_framework import serializers
from .models import EquipmentOrder  # Замените на имя вашей модели заказа

class EquipmentOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentOrder
        fields = '__all__'