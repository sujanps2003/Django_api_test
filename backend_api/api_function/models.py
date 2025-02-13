from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class HeartRate(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    bpm = models.IntegerField()
    recorded_at = models.DateTimeField(auto_now_add=True)



