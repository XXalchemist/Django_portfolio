from django.db import models

class Category(models.Model): #To define category of each blog
    name = models.CharField(max_length = 20)

class Post(models.Model): #To define each blog posts
    title = models.CharField(max_length = 255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True) #whenever instance of class is created
    last_modified = models.DateTimeField(auto_now = True) #whenever instance of class is saved i.e whenever an edit in post this time is updated
    categories = models.ManyToManyField('Category', related_name = 'posts') # many category can be assigned to many posts

class Comment(models.Model):
    author = models.CharField(max_length = 60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    post = models.ForeignKey('Post', on_delete = models.CASCADE)
    