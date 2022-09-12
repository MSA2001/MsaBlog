from blog.models import Article,Category

def recent_articles(request):
    recent_articles = Article.objects.order_by('-updated')
    categories = Category.objects.all()
    return ({'recent_articles':recent_articles, 'categories':categories })