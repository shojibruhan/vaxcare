from django_filters.rest_framework import FilterSet, filters, CharFilter, DateFilter
from .models import Booking, Vaccine


class VaccineFilterset(FilterSet):
    # doctor= CharFilter(field_name='doctor_id', lookup_expr='icontains') 
    class Meta:
        model= Vaccine
        fields= {
            # 'id': ['exact'],
            # 'doctor': ['contains'],
            'vaccine_name': ['contains'],
            # 'first_dose': ['contains'],
        }

'''

class VaccineFilterset(FilterSet):
    doctor = CharFilter(field_name="doctor__name", lookup_expr="icontains")  # Filter by doctor name
    first_dose = DateFilter(field_name="first_dose")  # Date field for calendar support

    class Meta:
        model = Vaccine
        fields = ['id', 'doctor', 'vaccine_name', 'first_dose']
'''
class BookingFilterset(FilterSet):
  
    class Meta:
        model= Booking
        fields= {
            'id': ['exact'],
            'patient': ['exact'],
            # 'vaccine': ['contains'],
            'status': ['contains'],
            
        }