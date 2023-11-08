from django.urls import path
from . import views

urlpatterns = [
    path('create_facility/', views.create_facility, name='create_facility'),
    path('create_energy_device/', views.create_energy_device, name='create_energy_device'),
    path('create_energy_audit/', views.create_energy_audit, name='create_energy_audit'),
    path('get_energy_audit/', views.get_audits, name='get_energy_audit'),
    path('get_energy_devices/', views.get_devices, name='get_energy_devices'),
    path('get_chat_prediction/',views.get_chat_prediction,name='get_predictions')
]
