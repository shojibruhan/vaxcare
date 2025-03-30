from django.shortcuts import render
from .models import Vaccine, Booking
from .serializers import CreateVaccineSerializers ,VaccineSerializers, BookingSerializers
from .filters import VaccineFilterset, BookingFilterset
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import DjangoModelPermissions


# Create your views here.
class VaccineViewSet(ModelViewSet):
    queryset= Vaccine.objects.all()
    serializer_class= VaccineSerializers
    filter_backends= [DjangoFilterBackend, SearchFilter]
    filterset_class= VaccineFilterset

    # def get_serializer_class(self):
    #     if self.request.method == 'POST':
    #         return CreateVaccineSerializers
    #     return VaccineSerializers
    
    # def get_serializer_context(self):
    #     return {'doctor_id': self.kwargs.get('doctor_pk')}

class BookingViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    http_method_names=['get', 'put', 'patch', 'post', 'delete']
    queryset= Booking.objects.all()
    serializer_class= BookingSerializers
