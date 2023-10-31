# energy_audit_app/serializers.py
from rest_framework import serializers
from .models import Facility, EnergyDevice, EnergyAudit

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'

class EnergyDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnergyDevice
        fields = '__all__'

class EnergyAuditSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnergyAudit
        fields = '__all__'