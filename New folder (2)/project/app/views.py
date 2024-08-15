from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
from .forms import DataItem
from .models import  Data

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
                messages.info(request, 'username is taken')
                return redirect('register.html')
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email is taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,
                                              email=email,
                                              password=password,
                                            )
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'password is not matching..')
            return redirect('register')
    return render(request, 'register.html')

def Login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,
                               password=password)
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

def Forms(request):
    if request.method == 'POST':
        frm = DataItem(request.POST, request.FILES)
        if frm.is_valid():
            frm.save()
            return redirect('/')
        
    else:
         frm = DataItem()

    return render(request, 'form.html',{'form':frm})

def Details(request):
    user_details=Data.objects.all()
    # user_details.id=pk
    return render(request, 'details.html',{'user_details':user_details})


def Edit(request,pk):
    instance_edit=Data.objects.get(pk=pk)
    if request.POST:
     frm=DataItem(request.POST, instance=instance_edit)
     if frm.is_valid():
         instance_edit.save()
         return redirect('details')
    else:
        frm=DataItem(instance=instance_edit)
    return render(request, 'form.html',{'form':frm})

def Delete(request,pk):
    instance=Data.objects.get(pk=pk)
    instance.delete() 
    user_details=Data.objects.all()
    return render(request, 'details.html',{'user_details':user_details})
 