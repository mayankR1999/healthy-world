from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_home, name = 'profile_home'),
    path('add_goal', views.add_goal, name = 'add_goal'),
]