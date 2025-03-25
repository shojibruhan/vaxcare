from django.shortcuts import render
from .models import Doctor, Patient
from .serializers import DoctorSerializer, PatientSerializer
from .filters import DoctorFilterset, PatientFilterset
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from .pagination import DefaultPagination
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class DoctorViewSet(ModelViewSet):
    queryset= Doctor.objects.select_related('user').all()
    serializer_class= DoctorSerializer
    filter_backends= [DjangoFilterBackend, SearchFilter]
    filterset_class= DoctorFilterset
    search_fields= ['user__first_name', 'user__last_name', 'specialization', 'user__email']
    pagination_class= DefaultPagination


class PatientViewSet(ModelViewSet):
    queryset= Patient.objects.select_related('user').all()
    serializer_class= PatientSerializer
    agination_class= DefaultPagination
    filter_backends= [DjangoFilterBackend, SearchFilter]
    filterset_class= PatientFilterset
    search_fields= ['user__first_name', 'user__last_name', 'user__email']