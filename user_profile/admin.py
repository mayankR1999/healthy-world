from django.contrib import admin
from .models import Goals, UserData

# Register your models here.

admin.site.register([Goals, UserData])