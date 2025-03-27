from rest_framework import serializers
from .models import Vaccine, Booking


class VaccineSerializers(serializers.ModelSerializer):
    class Meta:
        model= Vaccine
        fields= '__all__'


class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model= Booking
        fields= '__all__' 

