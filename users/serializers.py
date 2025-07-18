from rest_framework import serializers
from .models import Doctor, Patient, User
from .create_user import create_role
from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer, UserSerializer as DjoserUserSerializer





class BaseUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model= User
        fields= ['id', 'first_name', 'last_name', 'phone_number', 'email', 'password', 'address']


class UserCreateSerializer(DjoserUserCreateSerializer):
    password = serializers.CharField(write_only=True)
    class Meta(DjoserUserCreateSerializer.Meta):
        fields= ['email', 'password', 'first_name', 'last_name', 'address', 'phone_number']


class UserSerializer(DjoserUserSerializer):
    class Meta(DjoserUserSerializer.Meta):
        ref_name = 'CustomUser'
        # fields= ['email', 'password', 'first_name', 'last_name', 'address', 'phone_number']
        fields= ['email', 'first_name', 'last_name', 'address', 'phone_number', 'is_staff']
        read_only_fields= ['is_staff']


class DoctorSerializer(serializers.ModelSerializer):
    # user= BaseUserSerializer()
    user= UserCreateSerializer()
    # profile_picture= serializers.ImageField()
    class Meta:
        model= Doctor
        fields= ['id', 'user', 'specialization']
        # read_only_fields= ['user', ]
        # fields= ['id',  'specialization']

    # def create(self, validated_data):
    #     user_data= validated_data.pop('user')
    #     user= User.objects.create(**user_data)

    #     doctor= Doctor.objects.create(user= user, **validated_data)
    #     return doctor
    def create(self, validated_data):
        return create_role(validated_data, Doctor)


class PatientSerializer(serializers.ModelSerializer):
    user= BaseUserSerializer()
    # profile_picture= serializers.ImageField()
    class Meta:
        model= Patient
        fields= ['id', 'user', 'nid', 'date_of_birth', 'medical_history']

    def create(self, validated_data):
        return create_role(validated_data, Patient)
    


