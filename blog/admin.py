from django.contrib import admin
from .models import Article, Category, Comment, Message
# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'author', 'show_image')


@admin.register(Comment)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'show_image')


admin.site.register(Category)
admin.site.register(Message)