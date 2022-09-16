from django.shortcuts import render,get_object_or_404
from .models import Article,Category
from django.core.paginator import Paginator
# Create your views here.
def post_detail(request,slug):
    article = get_object_or_404(Article,slug=slug)
    recent_articles=Article.objects.all().order_by('-updated')[:4]
    return render (request,'blog/post-details.html',{ 'article':article , 'recent_articles':recent_articles  })

def articles_list(request):
    articles = Article.objects.all().order_by('-created')
    page_number = request.GET.get('page')
    paginator = Paginator(articles,2)
    object_list = paginator.get_page(page_number)
    return render(request,'blog/articles_list.html',{ 'articles':object_list })

def category_detail(request,pk=None):
    category=Category.objects.get(id=pk)
    articles= category.articles.all()    #article_set==>articles
    return render(request, 'blog/articles_list.html', {'articles': articles})