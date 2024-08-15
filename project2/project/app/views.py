from django.shortcuts import render,redirect
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def Home(request):
    return render(request, 'home.html')

def Register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        con_pass=request.POST['con_pass']
        if password == con_pass:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username_taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email is taken')
            else:
                user=User.objects.create_user(
                    username=username,
                    email=email, 
                    password=password
                    )
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'password is not matching...')
            return redirect('register')
    return render(request, 'register.html')

def Login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(
            username=username,
            password=password,
        )
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credential')
            return redirect('login')

    return render(request, 'login.html')

def Logout(request):
    auth.logout(request)
    return redirect('/')