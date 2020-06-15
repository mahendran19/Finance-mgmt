from django import forms
from .models import Income2,Expense2


class FormIncome2(forms.ModelForm):
    class Meta:
        model= Income2
        fields= ["salary"]

class FormExpense2(forms.ModelForm):
    class Meta:
        model= Expense2
        fields= ["Food","Rent","Transport","Others"]



