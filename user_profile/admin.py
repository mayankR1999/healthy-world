from django.contrib import admin
from .models import Goals, UserData, IsGoalActive

# Register your models here.

admin.site.register([Goals, UserData, IsGoalActive])