from operator import mod
from unicodedata import name
from venv import create
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class Contact(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=100)
    content=models.TextField()

    def __str__(self):
        return self.name


class datascience(models.Model):
    firstname=models.CharField(max_length=122)
    lastname=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=13)
    dob=models.DateField()
    gender=models.CharField(max_length=10)

    def __str__(self):
        return self.firstname +" "+ self.lastname

class python(models.Model):
    firstname=models.CharField(max_length=122)
    lastname=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=13)
    dob=models.DateField()
    gender=models.CharField(max_length=10)

    def __str__(self):
        return self.firstname +" "+ self.lastname

class webdev(models.Model):
    firstname=models.CharField(max_length=122)
    lastname=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=13)
    dob=models.DateField()
    gender=models.CharField(max_length=10)

    def __str__(self):
        return self.firstname +" "+ self.lastname



# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     USERNAME_FIELD: 'email'
#     REQUIRED_FIELDS: 