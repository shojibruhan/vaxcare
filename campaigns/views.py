from django.shortcuts import render
from .models import Vaccine, Booking
from .serializers import VaccineSerializers, BookingSerializers
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class VaccineViewSet(ModelViewSet):
    queryset= Vaccine.objects.all()
    serializer_class= VaccineSerializers



class BookingViewSet(ModelViewSet):
    queryset= Booking.objects.all()
    serializer_class= BookingSerializers