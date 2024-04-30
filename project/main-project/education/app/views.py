from django.shortcuts import render
from .forms import*
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView 

# Create your views here.
def home(request):
    return render(request,"index.html")


def about(request):
    d=student.objects.all()
    s={'data':d}
    
    return render(request,"page1.html",s)

def contact(request):
    return render(request,"page2.html")



def form1(request):
  f1=listForm()
  if(request.method=='POST'):
    f1=listForm(request.POST)
    if f1.is_valid():
      f1.save()
      return home(request)
    return render(request)
  return render(request,'form.html',{'form':f1})




class SignUpView(generic=CreateView.):
  form_class=UserCreationForm
  success_url=reverse_lazy('login')  
  template_name='registration/signup.html'






















  