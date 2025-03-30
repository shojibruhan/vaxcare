from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import Doctor, Patient
from campaigns.models import Vaccine
# Create your models here.
class DoctorReview(models.Model):
    doctor= models.ForeignKey(Doctor, on_delete=models.CASCADE)
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comments= models.TextField()
    ratings= models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now= True)

    def __str__(self):
        return f"Review of {self.doctor} by {self.user.get_full_name()}"
    

class CampaignReview(models.Model):
    vaccine= models.ForeignKey(Vaccine, on_delete=models.CASCADE, related_name='review')
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comments= models.TextField()
    ratings= models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now= True)

    def __str__(self):
        return f"Review of {self.vaccine} by {self.user.get_full_name()}"