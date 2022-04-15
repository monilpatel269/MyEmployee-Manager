from tkinter import Widget
from unicodedata import name
from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=20,null=False)
    location = models.CharField(max_length=40,default="")
    def __str__(self):
        return self.name
    

class Role(models.Model):
    name = models.CharField(max_length=30,null=False)
    def __str__(self):
        return self.name
    

class Employee(models.Model):
    firstName = models.CharField(max_length=30,null=False)
    lastName = models.CharField(max_length=30,default="")
    dept = models.ForeignKey(Department,on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hiredate = models.DateField()
    
    def __str__(self):
        return self.firstName  
    
class Contact(models.Model):
    contact_id = models.AutoField
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30, default="")
    phone = models.IntegerField(default="")
    desc = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
    
