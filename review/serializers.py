from .models import DoctorReview, CampaignReview
from users.models import Doctor, Patient
from rest_framework import serializers

class DoctorReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model= DoctorReview
        fields= ['id', 'name', 'comments', 'ratings']

    def create(self, validated_data):
        doctor_id= self.context['doctor_id']
        return DoctorReview.objects.create(doctor_id= doctor_id, **validated_data)

class CampaignReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model= CampaignReview
        fields= ['id', 'name', 'comments', 'ratings']

    def create(self, validated_data):
        vaccine_id= self.context['vaccine_id']
        return CampaignReview.objects.create(vaccine_id= vaccine_id, **validated_data)