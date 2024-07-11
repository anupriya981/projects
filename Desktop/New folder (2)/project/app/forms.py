from django.forms import ModelForm
from .models import DataItem

class DataForm(ModelForm):   
    class Meta:
        model =DataItem
        fields = '__all__'
 