from django import forms
from .models import Income

class FormIncome(forms.ModelForm):
    class Meta:
        model= Income
        fields= ["amount","user","mode"]