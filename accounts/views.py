from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def  user_login(request):
    if request.user.is_authenticated == True:
        return redirect('/')
    
    
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username ,password=password)
        print(user,)
        if user is not None:
            login(request,user)
            return redirect('/')
    return render(request, "accounts/login.html")

def user_logout(request):
    logout(request)
    return redirect('/')

def user_register(request):
    return render(request,'accounts/register.html')