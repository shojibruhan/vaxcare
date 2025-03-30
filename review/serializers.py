from .models import DoctorReview, CampaignReview
from users.models import Doctor, Patient
from rest_framework import serializers

class DoctorReviewSerializers(serializers.ModelSerializer):
    name= serializers.SerializerMethodField(method_name='get_user_name')
    class Meta:
        model= DoctorReview
        fields= ['id', 'name', 'comments', 'ratings']

    def get_user_name(self, obj):
        return obj.user.get_full_name()

    def create(self, validated_data):
        doctor_id= self.context['doctor_id']
        return DoctorReview.objects.create(doctor_id= doctor_id, **validated_data)

class CampaignReviewSerializers(serializers.ModelSerializer):
    name= serializers.SerializerMethodField(method_name='get_user_name')
    class Meta:
        model= CampaignReview
        fields= ['id', 'name', 'comments', 'ratings']

    def get_user_name(self, obj):
        return obj.user.get_full_name()


    def create(self, validated_data):
        vaccine_id= self.context['vaccine_id']
        user_id= self.context['user_id']
        return CampaignReview.objects.create(vaccine_id= vaccine_id, user_id=user_id, **validated_data)