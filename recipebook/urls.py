# Import
from django.urls import path
from . import views

# namespacing 
app_name = 'recipebook'

urlpatterns = [
    path('', views.IndexView.as_view(), name='homepage'),
    path('list/', views.ListView.as_view(), name='recipe_list'),
    path('<int:pk>/', views.DetailView.as_view(), name='recipe'),
    ]