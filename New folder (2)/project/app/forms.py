from django.forms import ModelForm
from .models import Data

class DataItem(ModelForm):
    class Meta:
        model = Data
        fields = '__all__'