from rest_framework import serializers
from .models import Doctor, Patient, User
from .create_user import create_role
from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer, UserSerializer as DjoserUserSerializer





class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ['id', 'first_name', 'last_name', 'phone_number', 'email', 'address']



class DoctorSerializer(serializers.ModelSerializer):
    user= UserSerializer()
    class Meta:
        model= Doctor
        fields= ['id', 'user', 'specialization', 'profile_picture']

    # def create(self, validated_data):
    #     user_data= validated_data.pop('user')
    #     user= User.objects.create(**user_data)

    #     doctor= Doctor.objects.create(user= user, **validated_data)
    #     return doctor
    def create(self, validated_data):
        return create_role(validated_data, Doctor)


class PatientSerializer(serializers.ModelSerializer):
    user= UserSerializer()
    class Meta:
        model= Patient
        fields= ['id', 'user', 'nid', 'date_of_birth', 'medical_history', 'profile_picture']

    def create(self, validated_data):
        return create_role(validated_data, Patient)
    

class UserCreateSerializer(DjoserUserCreateSerializer):
    class Meta(DjoserUserCreateSerializer.Meta):
        fields= ['email', 'password', 'first_name', 'last_name', 'address', 'phone_number']


class UserSerializer(DjoserUserSerializer):
    class Meta(DjoserUserSerializer.Meta):
        fields= ['email', 'password', 'first_name', 'last_name', 'address', 'phone_number']