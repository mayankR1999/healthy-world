from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Goals, UserData
import datetime

# Create your views here.

def profile_home(request):
    return render(request, 'profile_home.html')

def add_goal(request):
    goal_text = request.POST['goal']
    last_date = request.POST['target_date']
    date_created = str(datetime.datetime.now()).split(' ')[0]

    y1, m1, d1 = list(map(int, date_created.split("-")))

    new_goal = Goals()
    new_goal.description = goal_text
    new_goal.date_created = datetime.date(y1, m1, d1)
    new_goal.last_date = last_date
    new_goal.user = request.user

    new_goal.save()

    return HttpResponseRedirect(reverse('profile_home'))


def update_height(request):
    height = request.POST['height']
    user_info = UserData.objects.get(pk = request.user)
    user_info.height = height
    #user_info.save()

    return HttpResponseRedirect(reverse('profile_home'))

def update_weight(request):
    weight = request.POST['weight']

    user_info = UserData.objects.get(pk = request.user)
    user_info.weight = weight
    #user_info.save()

    return HttpResponseRedirect(reverse('profile_home'))

def update_gender(request):
    gender = request.POST['gender']
    user_info = UserData.objects.get(pk = request.user)
    user_info.gender = gender
    #user_info.save()

    return HttpResponseRedirect(reverse('profile_home'))

def update_birthday(request):
    DOB = request.POST['bday']
    user_info = UserData.objects.get(pk = request.user)
    user_info.DOB = DOB
    #user_info.save()

    return HttpResponseRedirect(reverse('profile_home'))
