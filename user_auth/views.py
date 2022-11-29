from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout



@csrf_protect
def user_login(request):
    return render(request, 'user_auth/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'user_auth/login.html')
def authenticate_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:register')
)
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('recipebook:homepage')
        )    
  

def user_reg(request):
    return render(request, 'user_auth/register.html')

def register(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    user = User.objects.create_user(username, None, password)
    login(request, user)
    return HttpResponseRedirect(
            reverse('recipebook:homepage')
        )
    
    
	         
