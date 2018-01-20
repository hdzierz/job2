from django import forms
from datetime import datetime, timedelta
from .models import *

class InvoiceForm(forms.Form):
    from_default_date = datetime.now() - timedelta(weeks=1)
    start_number = forms.IntegerField()
    frm = forms.DateField(label="From", input_formats=['%m/%d/%Y'], initial=(from_default_date.strftime("%m/%d/%Y")))
    to = forms.DateField(label="To", input_formats=['%m/%d/%Y'], initial=(datetime.now().strftime("%m/%d/%Y")))

    start_number.widget.attrs['class'] = 'form-control'
    frm.widget.attrs['class'] = 'form-control'
    to.widget.attrs['class'] = 'form-control'
