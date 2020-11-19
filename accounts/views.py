from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'home_page.html')

def login(request):
    pass

def register(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'register.html')

def logout(request):
    pass