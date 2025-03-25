from django.db import models
from users.models import Doctor, Patient
from uuid import uuid4
from datetime import timedelta
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Vaccine(models.Model):
    id= models.UUIDField(primary_key=True, default=uuid4, editable=False)
    doctor= models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='vaccination_campaigns')
    vaccine_name= models.CharField(max_length=200)
    first_dose= models.DateField()
    last_dose= models.DateField(blank=True, null=True)
    dose_interval= models.PositiveIntegerField(default=30, validators=[MinValueValidator(1)])


    def save(self, *args, **kwargs):
        if self.first_dose and not self.last_dose:
            self.last_dose= self.first_dose + timedelta(days= self.dose_interval)
        super().save(*args, **kwargs)

    
    def __str__(self):
        return f"{self.vaccine_name} campaign "



class Booking(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]
    patient= models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='my_vaccine')
    vaccine= models.ForeignKey(Vaccine, on_delete=models.CASCADE, related_name= 'bookings')
    dose_number= models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)], default=1)
    status= models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at= models.DateField(auto_now_add=True)
    dose_one= models.DateField()
    dose_two= models.DateField(blank=True, null=True)


    def save(self, *args, **kwargs):
        if self.vaccine and self.dose_one and self.dose_number == 1 and not self.dose_two:
            self.dose_two = self.dose_one + timedelta(days=self.vaccine.dose_interval)

        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.patient}'s vaccine: \"{self.vaccine}\" Dose: {self.dose_number}"