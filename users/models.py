from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager
from cloudinary.models import CloudinaryField

class User(AbstractUser):
    username= None
    email= models.EmailField(unique=True)
    address= models.TextField(blank=True, null=True)
    phone_number= models.CharField(max_length=15, blank=True, null=True)

    USERNAME_FIELD= 'email'     # use email instead of username
    REQUIRED_FIELDS= []
    
    objects= CustomUserManager()

    def __str__(self):
        return self.email
    

class Doctor(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor')
    specialization= models.CharField(max_length=300)
    profile_picture=CloudinaryField('images')


    def __str__(self):
        return self.user.get_full_name()

class Patient(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')
    nid= models.CharField(unique=True, max_length=15)
    date_of_birth= models.DateField()
    medical_history= models.TextField(blank=True, null=True)
    profile_picture=CloudinaryField('images')

    def __str__(self):
        return self.user.get_full_name()