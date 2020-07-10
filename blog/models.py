from django.db import models

class Category(models.Model): #To define category of each blog
    name = models.CharField(max_length = 20)

class Post(models.Model): #To define each blog posts
    title = models.CharField(max_length = 255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now= True)
    categories = models.ManyToManyField('Category', related_name = 'posts')