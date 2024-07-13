from django.db import models

# Create your models here.
class customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.TextField(max_length=10)
    img=models.ImageField(upload_to='media')
