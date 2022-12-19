from django.shortcuts import render
from blog.models import Article
# Create your views here.


def home(request):
    articles = Article.objects.all().order_by('?')
    recent_articles = Article.objects.all().order_by('-updated')[:4]
    return render(request, 'home/index-6.html', {'articles': articles, 'recent_articles': recent_articles})