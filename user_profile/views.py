from django.shortcuts import render

# Create your views here.

def profile_home(request):
    return render(request, 'profile_home.html')