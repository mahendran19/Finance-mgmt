from django.contrib import admin
from .models import User
from .models import Income
from .models import Expense

# Register your models here.
admin.site.register(User)
admin.site.register(Income)
admin.site.register(Expense)
