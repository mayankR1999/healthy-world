from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Goals, UserData, IsGoalActive
import datetime
from .features import check_achievements, is_on_time, pre_calculate

# Create your views here.

def profile_home(request):
    user = request.user
    # Handle Anonymous user
    user_goals = Goals.objects.filter(user = user)
    user_info = UserData.objects.get(pk = user)

    # new learning(can make new object values in django)
    for goal in user_goals:
        is_active = IsGoalActive.objects.get(pk = goal)
        goal.is_active = is_active.value

    pre_calculate(user_info)

    data = {
        'user_goals' : user_goals,
        'user_info' : user_info
    }
    return render(request, 'profile_home.html', data)

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

    is_active = IsGoalActive()
    is_active.goal = new_goal

    new_goal.save()
    is_active.save()

    return HttpResponseRedirect(reverse('profile_home'))

def goal_completed(request, id):
    goal = Goals.objects.get(id = id)
    user_info = UserData.objects.get(pk = request.user)
    is_goal_active = IsGoalActive.objects.get(pk = goal)
    
    if is_on_time(goal.last_date):
        user_info.tasks_completed += 1
        user_info.current_streak += 1
    else:
        user_info.current_streak = 0
    
    if user_info.current_streak > user_info.longest_streak:
        user_info.longest_streak = user_info.current_streak

    is_goal_active.value = False

    is_goal_active.save()
    user_info.save()

    return HttpResponseRedirect(reverse('profile_home'))

def update_height(request):
    height = request.POST['height']
    user_info = UserData.objects.get(pk = request.user)
    user_info.height = height
    user_info.save()

    return HttpResponseRedirect(reverse('profile_home'))

def update_weight(request):
    weight = request.POST['weight']

    user_info = UserData.objects.get(pk = request.user)
    user_info.weight = weight
    user_info.save()

    return HttpResponseRedirect(reverse('profile_home'))

def update_gender(request):
    gender = request.POST['gender']
    user_info = UserData.objects.get(pk = request.user)
    user_info.gender = gender
    user_info.save()

    return HttpResponseRedirect(reverse('profile_home'))

def update_birthday(request):
    DOB = request.POST['bday']
    user_info = UserData.objects.get(pk = request.user)
    user_info.DOB = DOB
    user_info.save()

    return HttpResponseRedirect(reverse('profile_home'))

def show_achievements(request):
    achievements = check_achievements(request)
    data = {
        'achievements': achievements
    }
    return render(request, 'user_achievements.html', data)
