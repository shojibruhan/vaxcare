from django.shortcuts import render
from .models import DoctorReview, CampaignReview
from .serializers import DoctorReviewSerializers, CampaignReviewSerializers
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class DoctorReviewViewSet(ModelViewSet):
    serializer_class= DoctorReviewSerializers

    def get_queryset(self):
        return DoctorReview.objects.filter(doctor_id= self.kwargs.get('doctor_pk'))
    
    def get_serializer_context(self):
        return {'doctor_id': self.kwargs.get('doctor_pk')}
    

class CampaignReviewViewSet(ModelViewSet):
    serializer_class= CampaignReviewSerializers

    def get_queryset(self):
        return CampaignReview.objects.filter(vaccine_id= self.kwargs.get('vaccine_pk'))

    def get_serializer_context(self):
        return {'vaccine_id': self.kwargs.get('vaccine_pk')}