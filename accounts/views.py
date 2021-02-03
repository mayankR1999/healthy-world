from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from user_profile.models import UserData
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

# Create your views here.

def home_page(request):
    return render(request, 'home_page.html')

def login(request):
    username = request.POST['user_name']
    password = request.POST['pass']

    user = auth.authenticate(username = username, password = password)
    if user:
        auth.login(request, user)
        return redirect('../profile')
    else:
        messages.info(request, "Username or password didn't match") # pass message
        return HttpResponseRedirect(reverse(home_page))

def register(request):
    if request.method == 'POST':

        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        user_name = request.POST["user_name"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        user = User.objects.create_user(username = user_name, email = email, password = pass1
                ,first_name = first_name, last_name = last_name)
        user.save()

        user_data = UserData()
        user_data.user = user
        user_data.save()

        return redirect('/')
        
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')