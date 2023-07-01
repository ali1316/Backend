from django.db import models
from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=100)
    building_number = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    manager = models.ForeignKey('Employee', null=True, blank=True, on_delete=models.SET_NULL)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
# Create your models here.
