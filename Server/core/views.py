from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .serializers import DeviceSerializer, LocationSerializer
from .models import Device, Location


# Create your views here.
class DeviceView(RetrieveUpdateDestroyAPIView):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()


class LocationView(RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
