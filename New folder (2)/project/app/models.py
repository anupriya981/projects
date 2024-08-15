from django.db import models

# Create your models here.
class Data(models.Model):
    name=models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    age=models.IntegerField()
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    image=models.ImageField(upload_to='media')