
from django import forms

class MonthlyJobForm(forms.Form):
    month = forms.CharField(label='Your name', max_length=100)
    year = forms.CharField(label='Your name', max_length=100) 

