from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

    
class Income(models.Model):
    
    #user=models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(),
        on_delete = models.CASCADE)
    salary = models.FloatField()

    
    

class Expense(models.Model):
    
    user = models.ForeignKey(get_user_model(),
        on_delete = models.CASCADE)
    expense = models.FloatField()
    
