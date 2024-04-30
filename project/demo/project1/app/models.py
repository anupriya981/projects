from django.db import models

# Create your models here.
class student(models.Model):
    roll_no=models.IntegerField()
    first_name=models.CharField( max_length=50)
    second_name=models.CharField(max_length=50)
    phone_no=models.IntegerField()
    
    
class student(models.Model):
    roll_no=models.IntegerField()
    first_name=models.CharField( max_length=50)
    second_name=models.CharField(max_length=50)
    phone_no=models.IntegerField()
