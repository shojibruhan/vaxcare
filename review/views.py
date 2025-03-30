from django.shortcuts import render
from .models import DoctorReview, CampaignReview
from .serializers import DoctorReviewSerializers, CampaignReviewSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions
from .permissions import IsReviewAuthorOrReadOnly
# Create your views here.


class DoctorReviewViewSet(ModelViewSet):
    serializer_class= DoctorReviewSerializers
    permission_classes= [IsReviewAuthorOrReadOnly]

    def get_queryset(self):
        return DoctorReview.objects.filter(doctor_id= self.kwargs.get('doctor_pk'))
    
    def get_serializer_context(self):
        return {'doctor_id': self.kwargs.get('doctor_pk')}
    
    def perform_create(self, serializer):
        serializer.save(user= self.request.user) 

class CampaignReviewViewSet(ModelViewSet):
    serializer_class= CampaignReviewSerializers
    permission_classes= [IsReviewAuthorOrReadOnly]

    def get_queryset(self):
        return CampaignReview.objects.filter(vaccine_id= self.kwargs.get('vaccine_pk'))

    def get_serializer_context(self):
        context= {
            'vaccine_id': self.kwargs.get('vaccine_pk'),
            'user_id': self.request.user.id
        }
        return context
        # return {'vaccine_id': self.kwargs.get('vaccine_pk')}