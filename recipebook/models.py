from django.db import models

class Recipe(models.Model):
    '''
    Recipe layout in database
        - Title: recipe name
        - Image: recipe image
        - Ingredients: list
        - Directions: step by step list
       
    Method to determine recently published questions

    String return for recipe
       
    '''    
    title = models.CharField(max_length=140)
    #pic = models.ImageField(blank=True, null=True, upload_to=None, height_field=None, width_field=None, max_length=100)
    pic = models.ImageField(blank=True, null=True)
    ingredients = models.TextField()
    directions = models.TextField()
    
    def __str__(self):
        return self.title

