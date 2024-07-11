from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
from .forms import DataForm
from .models import DataItem
# Create your views here.

def Home(request):
    user_details=DataItem.objects.all()
    return render(request, 'home.html',{'userdetail':user_details})

def Register(request):
    if request.method == 'POST':
       username=request.POST['username']
       email=request.POST['email']
       password=request.POST['password']
       con_pass=request.POST['con_pass']
       first_name=request.POST['first_name']
       last_name=request.POST['last_name'] 
       if password ==con_pass:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username is taken')
                return redirect(request, 'register')
            elif User.objects.filter(email=email).exists():
                messages.info('email is taken')
                return redirect('register')
            else:      
             user= User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password
             )
            user.save()
            return redirect('login')
            
       else:
           messages.info(request, 'password is not matchig...')
           return redirect('register')
    return render(request, 'register.html')

def Login(request):
    if request.method == 'POST':
       username=request.POST['username']
       password=request.POST['password'] 
       user=auth.authenticate(username=username, password=password)
       if user is not None:
          auth.login(request, user)
          return redirect('/')
       else:
          messages.info(request, 'invalid credential')
          return redirect('login')
    else:
     return render(request, 'login.html')
    
def Logout(request):
   auth.logout(request)
   return redirect('/')   


def Data(request):
   if request.POST:
         frm=DataForm(request.POST)
         if frm.is_valid():  
          frm.save()
         return redirect('/')

   else:
         frm=DataForm
   return render(request, 'datas.html', {'frm':frm})