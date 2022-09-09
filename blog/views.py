from django.shortcuts import render,get_object_or_404
from .models import Article
# Create your views here.
def post_detail(request,pk):
    article = get_object_or_404(Article,id=pk)
    return render (request,'blog/post-details.html',{ 'article':article })