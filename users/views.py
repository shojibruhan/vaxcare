from django.shortcuts import render
from .models import Doctor, Patient
from .serializers import DoctorSerializer, PatientSerializer
from .filters import DoctorFilterset, PatientFilterset
from .pagination import DefaultPagination
from api.permissions import IsAdminOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
# Create your views here.


class DoctorViewSet(ModelViewSet):
    queryset= Doctor.objects.select_related('user').all()
    serializer_class= DoctorSerializer
    filter_backends= [DjangoFilterBackend, SearchFilter]
    filterset_class= DoctorFilterset
    search_fields= ['user__first_name', 'user__last_name', 'specialization', 'user__email']
    pagination_class= DefaultPagination
    # permission_classes= [DjangoModelPermissions]

    @swagger_auto_schema(
            operation_summary="List of all Doctors"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class PatientViewSet(ModelViewSet):
    queryset= Patient.objects.select_related('user').all()
    serializer_class= PatientSerializer
    agination_class= DefaultPagination
    filter_backends= [DjangoFilterBackend, SearchFilter]
    filterset_class= PatientFilterset
    search_fields= ['user__first_name', 'user__last_name', 'user__email']
    # permission_classes= [IsAdminUser]