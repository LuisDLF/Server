from rest_framework.serializers import ModelSerializer

from Server.core.models import Device, Location


class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = ('__all__',)


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = ('__all__',)
