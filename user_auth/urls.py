from django.urls import path
from . import views

app_name = 'user_auth'
urlpatterns = [
    path('', views.user_reg, name='register'),
    path('register/', views.register, name='user_reg'),
    path('login/', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user,
    name='authenticate_user'),
    path('logout/', views.logout_view, name='logout'),
    ]
