from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def base(request):
    return render(request,'base.html')

def User_signUp(request):
     if request.method=='POST':
        user_name=request.POST.get('username')
        email=request.POST.get(' email')
        password1=request.POST.get('pass')
        password2=request.POST.get('c-pass')
        if password1==password2:
            if User.objects.filter(username=user_name,email=email,password=password1).exists():
                messages.info(request,'username is already exist!!!!')
                print('already have')
            else:
                new_user=User.objects.create_user(user_name,email,password1)
                new_user.save()
                return redirect(User_login)
        else:
            print('wrong password')
            return render(request,'signUp.html')


                
     return render(request,'signUp.html')


def User_login(request):
    if request.method=='POST':
        user_name=request.POST.get('username')
        password1=request.POST.get('pass1')
        user=authenticate(request,username=user_name,password=password1)
        if user is not None:
            login(request,user)
            return redirect(base)
        else:
            messages.info(request,'user not exist')
            print('user not exist')
            return redirect(User_login)
    return render(request,'login.html')

def User_logout(request):
    logout(request)
    return redirect(User_login)
 