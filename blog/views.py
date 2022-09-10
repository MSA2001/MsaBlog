from django.shortcuts import render,get_object_or_404
from .models import Article
# Create your views here.
def post_detail(request,slug):
    article = get_object_or_404(Article,slug=slug)
    return render (request,'blog/post-details.html',{ 'article':article })