from .models import DoctorReview
from users.models import Doctor, Patient
from rest_framework import serializers

class DoctorReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model= DoctorReview
        fields= ['id', 'name', 'description', 'ratings']

    def create(self, validated_data):
        doctor_id= self.context['doctor_id']
        return DoctorReview.objects.create(doctor_id= doctor_id, **validated_data)
