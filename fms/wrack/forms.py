from django import forms
from .models import Income1,Expense1


class FormIncome1(forms.ModelForm):
    class Meta:
        model= Income1
        fields= ["salary"]

class FormExpense1(forms.ModelForm):
    class Meta:
        model= Expense1
        fields= ["Food","Rent","Transport","Others"]



