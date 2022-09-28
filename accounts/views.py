from multiprocessing import context
from re import U
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import LoginForm
from accounts.forms import LoginForm
# Create your views here.


def  user_login(request):
    if request.user.is_authenticated == True:
        return redirect('home:home')
    
    
    if request.method =='POST':
      form = LoginForm(request.POST)
      if form.is_valid():
          user = User.objects.get(username=form.cleaned_data.get('username'))
          login(request,user)
          return redirect('home:home')
    else:
        form = LoginForm() 
      
    return render(request, "accounts/login.html",{'form':form})

def user_logout(request):
    logout(request)
    return redirect('home:home')

def user_register(request):
    context={'errors':[]}
    if request.user.is_authenticated == True:
        return redirect('home:home')
 
 
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')       
        password1=request.POST.get('password1')       
        password2=request.POST.get('password2')
        if password1 != password2:
            context['errors'].append('Passwords not match')
            return render(request,'accounts/register.html',context)
            
        user = User.objects.create(username=username,email=email,password=password1)
        login(request, user)
        return redirect('home:home')    
    return render(request,'accounts/register.html',{})