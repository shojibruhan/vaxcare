from django_filters.rest_framework import FilterSet, filters
from .models import Doctor, Patient, User


class DoctorFilterset(FilterSet):
    class Meta:
        model= Doctor
        fields= {
            'id': ['exact'],
            'user__email': ['exact'],
            'user__first_name': ['contains'],
            'user__last_name': ['contains'],
            'specialization': ['contains'],
        }

class PatientFilterset(FilterSet):
  
    class Meta:
        model= Patient
        fields= {
            'id': ['exact'],
            'user__email': ['exact'],
            'user__first_name': ['contains'],
            'user__last_name': ['contains'],
            
        }