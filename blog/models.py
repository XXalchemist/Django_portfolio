from django.db import models

class Category(models.Model): #To define category of each blog
    name = models.CharField(max_length = 20)
    
