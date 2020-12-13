from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=120, default='Medicine')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    img = models.ImageField(upload_to='media', null = True)
    date = models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
    

class ScientificResearch(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=120, default='Medicine')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    img = models.ImageField(upload_to='media', null = True)
    date = models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')


class Operation(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=120, default='Medicine')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    img = models.ImageField(upload_to='media', null = True)
    date = models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')