from django import forms
from .models import Income,Expense


class FormIncome(forms.ModelForm):
    class Meta:
        model= Income
        fields= ["salary"]

class FormExpense(forms.ModelForm):
    class Meta:
        model= Expense
        fields= ["expense"]



