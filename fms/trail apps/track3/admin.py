from django.contrib import admin

# Register your models here.
from .models import Income,Expense
admin.site.register(Expense)
admin.site.register(Income)