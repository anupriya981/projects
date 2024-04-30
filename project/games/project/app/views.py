from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib import auth 
from django.contrib.auth import authenticate,login as authlogin,logout as authlogout
from django.contrib.auth.decorators import login_required

from . models import GameInfo


# Create your views here.
# from django.contrib.auth import login,logout


def home(request):
    return render(request,"home.html")

def base(request):
    return render(request,'base.html')


def signup(request):
    if request.method=='POST':
        username=request.POST('username')
        password=request.POST('password')
        Conform_password=request.POST('Conform_password')
        email=request.POST('email')
        if password==Conform_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exist')
                return redirect('auth:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exist')
                return redirect('auth:register')

            user=User.objects.create_user(username=username,password=password,email=email)
            user.save()
            print("user created")
            return redirect('login')
        else:
            messages.info(request,"password not matched")
            return redirect('auth:register')
    return render(request, 'signup.html')
    


        # except Exception as e:
        #     error_message=str(e)


def authlogin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=auth.authenticate(email=email,password=password)
        if user is not None:
           auth.login(request,user)
           return redirect('home')
        else:
          messages.info(request,'invalid_credentials')
          return redirect("auth:login")
    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')

@login_required(login_url='login/')
def page(request):
    return render(request,'page.html')


def list(request):
    count=request.session.get('count',0)
    count=int(count)
    count=count+1
    request.session['count']=count



def home(request):
    if request.POST:
        game=request.POST.get('game')
        date=request.POST.get('date')
        desc=request.POST.get('summary')
        game_obj=GameInfo(game=game,date=date,description=desc)
        game_obj.save()
    return render(request,'home.html')

