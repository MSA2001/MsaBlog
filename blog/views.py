from django.shortcuts import render
from .models import Article
# Create your views here.
def post_detail(request,pk):
    article = Article.objects.get(id=pk)
    return render (request,'blog/post-details.html',{ 'article':article })