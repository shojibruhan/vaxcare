from django.shortcuts import render
from .models import Vaccine, Booking
from .serializers import CreateVaccineSerializers ,VaccineSerializers, BookingSerializers, BookListSerializers
from .filters import VaccineFilterset, BookingFilterset
from review.permissions import IsReviewAuthorOrReadOnly
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser, IsAuthenticated



class VaccineViewSet(ModelViewSet):
    # queryset= Vaccine.objects.all()
    # serializer_class= VaccineSerializers
    filter_backends= [DjangoFilterBackend, SearchFilter]
    filterset_class= VaccineFilterset
  


    def get_queryset(self):
        queryset= Vaccine.objects.select_related('doctor__user')
        if self.request.user.is_staff:
            return queryset.all()
        # if hasattr(self.request.user, 'doctor'):
        if self.request.user.doctor:
            return queryset.filter(doctor= self.request.user.doctor)
        return queryset.none()
  


    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateVaccineSerializers
        return VaccineSerializers
    
    def get_serializer_context(self):
        if hasattr(self.request.user, 'doctor'):
            return {'doctor_id': self.request.user.doctor.id}
        
    def get_permissions(self):
        if self.request.method in ['POST', 'PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticated()]

class BookingViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    # http_method_names=['get', 'put', 'patch', 'post', 'delete']
    queryset= Booking.objects.all()
    # serializer_class= BookingSerializers
    permission_classes= [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return BookListSerializers
        return BookingSerializers

   

    def get_serializer_context(self):
        return {'patient_id': self.request.user.patient.id, 'user_id': self.request.user.id}


class BookListViewSet(ModelViewSet):
    serializer_class= BookListSerializers
    filter_backends= [SearchFilter]
    search_fields= ['status']
    http_method_names= ['get']

    def get_queryset(self):
        queryset = Booking.objects.select_related('patient__user', 'vaccine__doctor')
        if self.request.user.is_staff:
            return queryset.all()
        return queryset.filter(patient__user= self.request.user)
    
    # def get_serializer_class(self):
    #     if self.request.method == 'POST':
    #         return BookingSerializers
    #     return BookListSerializers
        
    # def get_serializer_context(self):
    #     return {'patient_id': self.request.user.patient.id, 'user_id': self.request.user.id}
    # def get_permissions(self):
    #     if self.request.method in ['PATCH', 'PUT', 'DELETE']:
    #         return [IsAdminUser()]
    #     return [IsAuthenticated()]
        
    
    
    