from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class category(models.Model):
    category_name=models.CharField(max_length=250)
    def __str__(self):
        return self.category_name



class product(models.Model):
    product_name=models.CharField(max_length=250)
    image=models.ImageField(upload_to="image", null=True)
    price=models.IntegerField()
    descrption=models.CharField(max_length=250)
    category= models.ForeignKey(category, on_delete=models.CASCADE, null=True)

class cart(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    User=models.ForeignKey(User,on_delete=models.CASCADE)

