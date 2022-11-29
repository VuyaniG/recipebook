from django.db import models

class Recipe(models.Model):
    '''
    Recipe layout in database
    :param models.Model: The models class

    String return for recipe
       
    '''    
    title = models.CharField(max_length=140)
    #pic = models.ImageField(blank=True, null=True, upload_to=None, height_field=None, width_field=None, max_length=100)
    pic = models.ImageField(blank=True, null=True)
    ingredients = models.TextField()
    directions = models.TextField()
    
    def __str__(self):
        '''
        Returns object as string
        :return: object as string
        :rtype: string'''
        return self.title

