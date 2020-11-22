from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_home, name = 'profile_home'),
    path('add_goal', views.add_goal, name = 'add_goal'),
    path('update_height', views.update_height, name = 'update_height'),
    path('update_weight', views.update_weight, name = 'update_weight'),
    path('update_gender', views.update_gender, name = 'update_gender'),
    path('update_birthday', views.update_birthday, name = 'update_birthday'),
    path('achievements', views.show_achievements, name = 'achievements'),
    path('goal_completed/<int:id>', views.goal_completed, name = 'goal_completed'),
]