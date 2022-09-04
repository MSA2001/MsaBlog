from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class profile(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    melicode=models.CharField(max_length=12)
    fathersname=models.CharField(max_length=20)
    image=models.ImageField(upload_to='profile/image',blank=True,null=True)
    
    def __str__(self):
        return self.user.username