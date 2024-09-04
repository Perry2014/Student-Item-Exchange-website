from django.db import models

# Create your models here.

class products(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    price=models.IntegerField()
    image=models.URLField()
    sellername=models.CharField(max_length=100)
    sellermobileNum=models.CharField()