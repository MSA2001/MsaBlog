from logging import PlaceHolder
from tkinter import CASCADE
from turtle import title

from django.utils.html import format_html
from unicodedata import category

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='articles')
    title = models.CharField(max_length=70)
    slug = models.SlugField(blank=True, unique=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/articles')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug=slugify(self.title)
        super(Article, self).save()
    
    def __str__(self):
        return f"{self.title} - {self.body[:30]} "

    def show_image(self):
        return format_html(f"<img src='{self.image.url}' width='55px' height='33px'> ")


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{ self.user.username  } - { self.body[:25] }"

    def show_image(self):
        return format_html(f"<img src='{self.user.profile.image.url}' width='45px' height='45px'> ")


class Message(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
