from django.shortcuts import render,redirect
from .forms import Lists
from .models import List


# Create your views here.
def Home(request):
    return render(request, 'home.html')

def Form(request):
    if request.method == 'POST':
        frm = Lists(request.POST, request.FILES)
        if frm.is_valid():
            frm.save()
            return redirect('/')
    else:
        frm = Lists()
    return render(request, 'form.html',{'form':frm})

def Details(request):
    form=List.objects.all()
    return render(request, 'details.html', {'Form':form})

def Person(request,pk):
    instance=List.objects.get(pk=pk)
    return render(request, 'person.html',{'list':instance})

def Delete(request,pk):
    instance=List.objects.get(pk=pk)
    instance.delete()
    return render(request, 'details.html',{'list':instance}) 

def Edit(request,pk):
    instance_edit=List.objects.get(pk=pk)
    if request.method == 'POST':
        frm = Lists(request.POST,request.FILES ,instance=instance_edit)
        if frm.is_valid():
            instance_edit.save()
            return redirect('details')
    else:
        frm = Lists(instance=instance_edit)
    return render(request, 'form.html',{'form':frm})