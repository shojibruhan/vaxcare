from django.shortcuts import render
from .models import DoctorReview
from .serializers import DoctorReviewSerializers
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class DoctorReviewViewSet(ModelViewSet):
    queryset= DoctorReview.objects.all()
    serializer_class= DoctorReviewSerializers

    def get_queryset(self):
        return DoctorReview.objects.filter(doctor_id= self.kwargs.get('doctor_pk'))
    
    def get_serializer_context(self):
        return {'doctor_id': self.kwargs.get('doctor_pk')}
