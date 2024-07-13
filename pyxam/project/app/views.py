from django.shortcuts import render
from .models import customer
from .forms import Customer

# Create your views here.
def Home(request):
    details=customer.objects.all()
    return render(request, 'home.html',{'detail':details})

def Datas(request):
    return render(request, 'datas.html')


def Forms(request):
    if request.method == 'POST':
        frm=Customer(request, post)
        if frm.is_valid:
            frm.save()
        else:
            frm=Customer
    return render(request, 'forms.html')