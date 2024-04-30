from django import forms
from .models import*
from django import forms
class listForm(forms.Form):
    class meta:
        model=list
        field='__all__'
    
    
    
   