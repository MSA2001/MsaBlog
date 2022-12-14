import email
from multiprocessing import context
from re import U
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import profile
from accounts.forms import LoginForm, RegisterForm, UserEditForm, UserPicForm
# Create your views here.


def user_login(request):

    if request.user.is_authenticated == True:
        return redirect('home:home')
    
    if request.method =='POST':
      form = LoginForm(request.POST)
      if form.is_valid():
          user = User.objects.get(username=form.cleaned_data.get('username'))
          login(request, user)
          return redirect('home:home')
    else:
        form = LoginForm() 
      
    return render(request, "accounts/login.html", {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home:home')


def user_register(request):
    if request.user.is_authenticated:
        return redirect('home:home')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create(username=form.cleaned_data.get('username'), email=form.cleaned_data.get('email'))
            login(request, user)
            return redirect('home:home') 
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_edit(request):
    user = request.user
    form = UserEditForm(instance=user)
    if request.method == 'POST':
        form = UserEditForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'accounts/edit.html', {'form': form})


def user_pic(request):
    if request.method == 'POST':
        form = UserPicForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile.objects.update(image=form.cleaned_data['image'])
            form.save()

            img_object = form.instance
            return render(request, 'accounts/profilepic.html', {'form': form, 'img_obj': img_object})
    else:
        form = UserPicForm()
    return render(request, 'accounts/profilepic.html', {'form': form})

