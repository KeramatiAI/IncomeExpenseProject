from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11,blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    postal_code = models.TextField(max_length=10,blank=True,null=True)
    def __str__(self):
        return "{}-{}".format(self.user,self.phone_number)

class Income(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=0)
    description = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{}-{}-{}-{}".format(self.user,self.date,self.amount,self.description)

class Expense(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10,decimal_places=0)
    description = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{}-{}-{}-{}".format(self.user,self.date,self.amount,self.description)
