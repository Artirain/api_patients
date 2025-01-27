from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='patient')


    def __str__(self):
        return self.username



class Patient(models.Model):
    date_of_birth = models.DateField()
    diagnoses = models.JSONField(default=list)  # храним список диагнозов как массив строк
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Patient {self.id}"
