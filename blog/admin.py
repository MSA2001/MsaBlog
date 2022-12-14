from django.contrib import admin
from .models import Article, Category, Comment, Message, Like
# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'author',)


@admin.register(Comment)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


admin.site.register(Category)
admin.site.register(Message)
admin.site.register(Like)