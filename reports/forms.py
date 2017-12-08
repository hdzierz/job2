
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



from django import forms
from  master_files.models import Region, Route


pmps  = [("1","with PMP"),("2","without PMP"),("3","Descriptions without PMP"),("4","Area Totals")]
types = [("total","Total"),("farmers","Farmers"),("lifestyle","L/style"),("diary","Diary"),("sheep","Sheep"),("beef","Beef"),
         ("sb","S/B"),("db","D/B"),("hort","Hort"),("fat90","Fat@90%"),("rmt","RMT"),("rmrr","RM RR"),("rmf","RM F"),("rmd","RM D")]




class PmpUpdatedForm(forms.Form):

    pmp   = forms.ChoiceField(label="PMP", choices=pmps)

    type = forms.ChoiceField(label="Type", choices=types)

    # type = forms.ModelChoiceField(label="Type", queryset=Route.objects.all())

    region = forms.ModelChoiceField(label=("Select Region"), queryset=Region.objects.all())

    rmni    = forms.BooleanField(label=("Show RM NI "), required=False)

    rmsi = forms.BooleanField(label=("Show RM SI "), required=False)