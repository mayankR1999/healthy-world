from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Goals
import datetime

# Create your views here.

def profile_home(request):
    return render(request, 'profile_home.html')

def add_goal(request):
    goal_text = request.POST['goal']
    last_date = request.POST['target_date']
    print(last_date)
    date_created = str(datetime.datetime.now())
    date_created = date_created.split(' ')[0]

    y1, m1, d1 = list(map(int, date_created.split("-")))
    y2, m2, d2 = list(map(int, last_date.split("-")))

    new_goal = Goals()
    new_goal.description = goal_text
    new_goal.date_created = datetime.date(y1, m1, d1)
    new_goal.last_date = datetime.date(y2, m2, d2)
    new_goal.user = request.user

    new_goal.save()

    return HttpResponseRedirect(reverse('profile_home'))