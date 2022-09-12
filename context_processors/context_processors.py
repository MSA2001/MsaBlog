from blog.models import Article

def recent_articles(request):
    recent_articles = Article.objects.order_by('-updated')
    return ({'recent_articles':recent_articles})