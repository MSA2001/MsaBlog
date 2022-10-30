from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    image = models.ImageField(upload_to='profile/image', blank=True, null=True, default='images/noprofile.jpg')
    
    def __str__(self):
        return self.user.username