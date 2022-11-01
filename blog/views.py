import email
from email import message
from multiprocessing import context

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse


from .models import Article, Category, Comment, Message ,Like
from django.core.paginator import Paginator
from .forms import  MessageForm
from django.views.generic import View, DetailView, ListView
from django.views.generic.base import TemplateView, View, RedirectView
# Create your views here.


def post_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    recent_articles = Article.objects.all().order_by('-updated')[:4]
    category = article.category.all()
    if request.user.is_authenticated:
        if request.user.likes.filter(article__slug=slug, user_id=request.user.id).exists():
            like = True
        else:
            like = False
    else:
        return render(request, 'blog/article_detail.html',
                      {'article': article, 'recent_articles': recent_articles, 'category': category})

    if request.method == 'POST':
        body = request.POST.get('body')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(body=body, user=request.user, article=article, parent_id=parent_id)
        return redirect("blog:detail", slug=slug)


    return render(request, 'blog/article_detail.html', {'article': article, 'recent_articles': recent_articles, 'category': category, 'like':like })




def articles_list(request):
    articles = Article.objects.all().order_by('-created')
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    object_list = paginator.get_page(page_number)
    for article in articles:
        category = article.category.all()

    return render(request, 'blog/articles_list.html', {'articles': object_list, 'category': category})



def category_detail(request, pk=None):
    category = Category.objects.get(id=pk)
    articles = category.articles.all()
    return render(request, 'blog/articles_list.html', {'articles': articles})


def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    object_list = paginator.get_page(page_number)
    return render(request, 'blog/articles_list.html', {'articles': object_list})

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


def like(request, slug, pk):
    if request.user.is_authenticated:
        try:
            like = Like.objects.get(article__slug=slug, user_id=request.user.id)
            like.delete()

        except:
            Like.objects.create(article_id=pk, user_id=request.user.id)

        return redirect('blog:detail', slug)






