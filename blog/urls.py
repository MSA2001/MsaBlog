from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('detail/<slug:slug>', views.post_detail, name='detail'),
    path('list', views.articles_list, name='articles_list'),
    path('category/<int:pk>', views.category_detail, name='category_detail'),
    path('search/', views.search, name='search_articles'),
    path('contact', views.contact_us, name='contact_us'),
    path('about', views.About, name='about'),
    path('Like/<slug:slug>/<int:pk>', views.like, name='like')


]
