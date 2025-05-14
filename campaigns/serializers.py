from rest_framework import serializers

from .models import Vaccine, Booking
from users.models import Doctor


class CreateVaccineSerializers(serializers.ModelSerializer):
    class Meta:
        model= Vaccine
        fields= ['id', 'vaccine_name', 'first_dose', 'dose_interval']
    
    def create(self, validated_data):
        doctor_id= self.context['doctor_id']
        if self.validated_data:
            return Vaccine.objects.create(doctor_id= doctor_id, **validated_data)

        



class VaccineSerializers(serializers.ModelSerializer):
    # doctor= serializers.CharField(source= 'doctor.user.get_full_name')
    doctor_name= serializers.SerializerMethodField(method_name='get_doctor_name')
    class Meta:
        model= Vaccine
        # fields= '__all__' 
        fields= ['id', 'doctor', 'doctor_name', 'vaccine_name', 'first_dose', 'dose_interval', 'last_dose']
    
    def get_doctor_name(self, vaccine):
        return vaccine.doctor.user.get_full_name()


class BookingSerializers(serializers.ModelSerializer):
    patient_name= serializers.SerializerMethodField(method_name='get_patient_name')
    vaccine_name= serializers.SerializerMethodField(method_name='get_vaccine_name')
    class Meta:
        model= Booking
        # fields= '__all__' 
        fields= ['id', 'patient_name', 'vaccine', 'vaccine_name', 'dose_number', 'status', 'created_at', 'dose_one', 'dose_two']

    dose_two= serializers.DateField(read_only= True)
    

    def get_patient_name(self, patient_name):
        return patient_name.patient.user.get_full_name()
        # return patient_name.user.get_full_name()
    
    def get_vaccine_name(self, vaccine_name):
        return vaccine_name.vaccine.vaccine_name
    
    def create(self, validated_data):
        
        patient_id= self.context.get('patient_id')
        # user_id= self.context.get('user_id')
        
        if self.validated_data:
            return Booking.objects.create(patient_id= patient_id, **validated_data)

    # def create(self, validated_data):
    #     print("validate Data: \n\n", validated_data)
    #     try:
    #         patient_id = self.context.get('patient_id')
            
    #         return Booking.objects.create(patient_id=patient_id, **validated_data)
    #     except Exception as e:
    #         print("Booking Create Error:", e)
    #         raise e

      
    # vaccine= serializers.CharField(source= 'vaccine.vaccine_name')
    # patient= serializers.CharField(source= 'patient.user.get_full_name')


class BookListSerializers(serializers.ModelSerializer):
    patient_name= serializers.SerializerMethodField(method_name='get_patient_name')
    class Meta:
        model= Booking
        fields= ['id', 'patient_name', 'vaccine', 'dose_number', 'created_at', 'status', 'dose_one', 'dose_two', ]
       
    
    def get_patient_name(self, patient_name):
        return patient_name.patient.user.get_full_name()
    
    def create(self, validated_data):
        print("validate Data: \n\n", validated_data)
        try:
            patient_id = self.context.get('patient_id')
            
            return Booking.objects.create(patient_id=patient_id, **validated_data)
        except Exception as e:
            print("Booking Create Error:", e)
            raise e