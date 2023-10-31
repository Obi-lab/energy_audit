# energy_audit_app/models.py
from django.db import models
from accounts.models import UserAccount

class Facility(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class EnergyDevice(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=100)
    rating = models.FloatField()

class EnergyAudit(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE,default=1)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    devices = models.ManyToManyField(EnergyDevice)
    operation_hours = models.CharField(default='N/A' ,max_length=50)
    audit_result = models.FloatField(null=True, blank=True)
