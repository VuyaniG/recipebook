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
    """This method will be used to request the login page template

        :returns: render for login.html

        :rtype: function
    """
    return render(request, 'user_auth/login.html')

def logout_view(request):
    """This method will be used to logout logged in user and to request the login page template

        :returns: render for login.html

        :rtype: function
    """
    logout(request)
    return render(request, 'user_auth/login.html')
def authenticate_user(request):
    """This method will be used to authenticate user credentials through the backend
        if user does not exist register page is loaded, if credentials are authenticated user is logged in and directed to homepage

        :returns: HttpResponseRedirect to redirect to url

        :rtype: class
    """
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
    """This method will be used to request the registration page template

        :returns: render for register.html

        :rtype: function
    """
    return render(request, 'user_auth/register.html')

def register(request):
    """This method will be used to register new user credentials through the backend
        and log user in. User is then directed to homepage

        :returns: HttpResponseRedirect to redirect to url

        :rtype: class
    """
    username = request.GET.get('username')
    password = request.GET.get('password')
    user = User.objects.create_user(username, None, password)
    login(request, user)
    return HttpResponseRedirect(
            reverse('recipebook:homepage')
        )
    
    
	         
