
from django import forms

class MonthlyJobForm(forms.Form):
    month = forms.CharField(label='Your name', max_length=100)
    year = forms.CharField(label='Your name', max_length=100) 




from bootstrap_datepicker.widgets import DatePicker
from  master_files.models import Region

Choice = Region.objects.all()

class RegionBibleForm(forms.Form):

    region   = forms.ModelChoiceField(label=("Select Region"), queryset=Region.objects.all() )

    date     = forms.DateField(widget=DatePicker(options={"format": "mm/dd/yyyy","autoclose": True}),  required=False)

    homeno   = forms.BooleanField(label=("Home No"), required=False)

    mobileno   = forms.BooleanField(label=("Mobile No"),  required=False)




from  master_files.models import Region


class PmpUpdatedForm(forms.Form):

    pmp   = forms.ModelChoiceField(label=("Select..."), queryset=Region.objects.all() )

    type = forms.ModelChoiceField(label=("Select Type"), queryset=Region.objects.all())

    region = forms.ModelChoiceField(label=("Select Region"), queryset=Region.objects.all())

    rmni    = forms.BooleanField(label=("Show RM NI "), required=False)

    rmsi = forms.BooleanField(label=("Show RM SI "), required=False)