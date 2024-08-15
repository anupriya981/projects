from django.db import models

# Create your models here.
class List(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    place=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    image=models.ImageField(upload_to='media')
    