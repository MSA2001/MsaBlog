import email
from email import message
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Article, Category, Comment, Message
from django.core.paginator import Paginator
from .forms import  MessageForm
from django.views.generic import View, DetailView, ListView
from django.views.generic.base import TemplateView, View, RedirectView
# Create your views here.


def post_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    recent_articles = Article.objects.all().order_by('-updated')[:4]

    if request.method == 'POST':
        body = request.POST.get('body')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(body=body, user=request.user, article=article, parent_id=parent_id)

    return render(request, 'blog/article_detail.html', {'article': article, 'recent_articles': recent_articles})




def articles_list(request):
    articles = Article.objects.all().order_by('-created')
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    object_list = paginator.get_page(page_number)
    return render(request,'blog/articles_list.html', {'articles': object_list})



def category_detail(request, pk=None):
    category=Category.objects.get(id=pk)
    articles= category.articles.all()
    return render(request, 'blog/articles_list.html', {'articles': articles})


def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    object_list = paginator.get_page(page_number)
    return render(request, 'blog/articlذs_list.html', {'articles': object_list})

def contact_us(request):
    if request.method == 'POST':  
        form = MessageForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.email = request.user.email
            instance.save()
            return redirect('home:home')
    else:
        form = MessageForm        
    return render(request, 'blog/contact_us.html', {'form': form})

def About(request):
    return render(request, 'blog/about.html')





