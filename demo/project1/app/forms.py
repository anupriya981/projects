from django import forms
from .models import*

class listForm(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'
