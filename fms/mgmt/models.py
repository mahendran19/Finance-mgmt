from django.db import models

class User(models.Model):
    id=models.IntegerField(primary_key=True)    
    username = models.CharField(max_length=250)
    password =models.CharField(max_length=250)    
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=64)
    Email = models.EmailField()
    gender = models.CharField(max_length=250)
    
class Income(models.Model):
    id = models.IntegerField(primary_key=True) 
    mode = models.CharField(max_length=250)
    amount = models.FloatField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    addedon = models.DateTimeField()

class Expense(models.Model):
    id = models.IntegerField(primary_key=True) 
    mode = models.CharField(max_length=250)
    amount = models.FloatField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    addedon = models.DateTimeField()

    