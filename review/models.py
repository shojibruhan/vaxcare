from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import Doctor
from campaigns.models import Vaccine
# Create your models here.
class DoctorReview(models.Model):
    doctor= models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name= models.CharField(max_length=100)
    comments= models.TextField()
    ratings= models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"Review of {self.doctor} by {self.name}"
    

class CampaignReview(models.Model):
    vaccine= models.ForeignKey(Vaccine, on_delete=models.CASCADE, related_name='review')
    name= models.CharField(max_length=100)
    comments= models.TextField()
    ratings= models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"Review of {self.vaccine} by {self.name}"