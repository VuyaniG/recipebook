# Imports
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, path 
from django.views import generic
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.utils import timezone
from .models import Recipe
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required




class IndexView(TemplateView):
    '''link template file Home.html to view'''
    
    template_name = 'recipebook/Home.html'
    context_object_name = 'recipe_list'
    
    def get_context_data(self, **kwargs):
        
            context = super().get_context_data(**kwargs)
            context['recipe_list'] = Recipe.objects.all()[:2]
            return context  
        
                 

class ListView(generic.ListView):
    '''link template file recipelist.html to view'''
    
    template_name = 'recipebook/recipelist.html'
    context_object_name = 'recipe_list'
    
    def get_queryset(self):
        """
        """
        return Recipe.objects.all()
# recipe
class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipebook/recipe.html'
    context_object_name = 'recipe'
    
       