from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    height = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    DOB = models.DateField(default = datetime.date(2000, 1, 1))
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length = 6, null=True)
    reward = models.CharField(max_length = 25, default = 'NOVICE')
    tasks_completed = models.IntegerField(default = 0)
    current_streak = models.IntegerField(default = 0)
    longest_streak = models.IntegerField(default = 0)

class Goals(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length = 500)
    date_created = models.DateField()
    last_date = models.DateField()

# class Achievements(models.Model): 

# class Settings(models.Model):
