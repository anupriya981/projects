from django.forms import ModelForm
from .models import  List

class Lists(ModelForm):   
    class Meta:
        model = List
        fields = "__all__"