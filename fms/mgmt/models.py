from django.db import models

# Create your models here.


class ContactForm(models.Model):
    salary=models.IntegerField()
    others=models.IntegerField()
    Totalsalary=models.IntegerField()