from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import LocationSerializer
from .serializers import EquipmentSerializer
from .models import Location
from .models import Equipment


class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all().order_by('id')
    serializer_class = LocationSerializer 

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all().order_by('id')
    serializer_class = LocationSerializer

class EquipmentList(generics.ListCreateAPIView):
    queryset = Equipment.objects.all().order_by('id')
    serializer_class = EquipmentSerializer 

class EquipmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all().order_by('id')
    serializer_class = EquipmentSerializer
