from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Provider(User):
    name = models.CharField(max_length=250, default='')
    phone = models.CharField(max_length=250, default='')
    rating = models.IntegerField(default=0)

class Consumer(User):
    name = models.CharField(max_length=250, default='')
    phone = models.CharField(max_length=250, default='')
    adress = models.TextField(default=0)
    geo_location = models.CharField(max_length=250, default='')

class Category(models.Model):
    name = models.CharField(max_length=250, default='')

class Product(models.Model):
    name = models.CharField(max_length=250, default='')
    image = models.ImageField(upload_to='product')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)