from dataclasses import field
from rest_framework import serializers
from .models import Location
from .models import Equipment


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name', 'address',)
        
class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ('id', 'type', 'brand', 'model', 'quantity', 'rented', 'location',)
