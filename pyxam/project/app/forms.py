from django.forms import ModelForm
from .models import  customer
class Customer:
    class Meta:
        model=customer
        field='__all__'