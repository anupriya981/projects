from django.shortcuts import render
from .models import*
from .forms import*


# Create your views here.
def home(request):
    return render(request,"page.html")

def about(request):
     d=student.objects.all()
     s={'data':d}
     return render(request,"page1.html")
 
 
 

