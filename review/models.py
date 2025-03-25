from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import Doctor
# Create your models here.
class DoctorReview(models.Model):
    doctor= models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name= models.CharField(max_length=100)
    description= models.TextField()
    ratings= models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"Review of {self.doctor} by {self.name}"