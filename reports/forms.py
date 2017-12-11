from master_files.models import Address
from django import forms

class MonthlyJobForm(forms.Form):
    month = forms.CharField(label='Your name', max_length=100)
    year = forms.CharField(label='Your name', max_length=100) 


class SummaryDeliveryInstructionsForm(forms.Form):
    frm = forms.DateField(label='Start Date')
    to = forms.DateField(label="Final Date")
    dist = forms.ModelChoiceField(\
            queryset=Address.objects.filter(typ__name="lbm_dist")
            )
    comment = forms.CharField(min_length=255, label="Comment")

