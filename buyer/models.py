from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class BuyerTable(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    contact = models.CharField(max_length=20,blank=True)
    gender = models.CharField(max_length=20,blank=True)
    address = models.CharField(max_length=30,blank=True)


    def __str__(self):
        return self.user.username

class Report(models.Model):
    username=models.CharField(max_length=20,blank=False)
    email=models.CharField(max_length=30,blank=False)
    desc=models.TextField(max_length=500,blank=False)

    def __str__(self):
        return self.username
