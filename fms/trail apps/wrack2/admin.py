from django.contrib import admin

# Register your models here.
from .models import Income1,Expense1
admin.site.register(Expense1)
admin.site.register(Income1)