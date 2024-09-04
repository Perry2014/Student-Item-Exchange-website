from django.db import models

# Create your models here.
class profile(models.Model):
    email=models.EmailField()
    mobile_number=models.CharField()
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=150,primary_key=True)
    password=models.CharField(max_length=50)


class students(models.Model):
    email=models.EmailField(primary_key=True)
    name=models.CharField(max_length=100)
    branch=models.CharField(max_length=20)
    registration_num=models.CharField(max_length=20)