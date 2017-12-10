
from django import forms

class MonthlyJobForm(forms.Form):
    month = forms.CharField(label='Your name', max_length=100)
    year = forms.CharField(label='Your name', max_length=100) 






from django import forms
from  master_files.models import Region, Route


pmps  = [("1","with PMP"),("2","without PMP"),("3","Descriptions without PMP"),("4","Area Totals")]
types = [("num_total","Total"),("num_farmers","Farmers"),("num_lifestyle","Life Style"),("num_diaries","Diary"),("num_sheep","Sheep"),("num_beef","Beef"),
         ("num_sheepbeef","Sheep Beef"),("num_diarybeef","Diary Beef"),("num_hort","Hort"),("num_nzfw","Fat@90%"),("rmt","RMT"),("rm_rr","RM RR"),("rm_f","RM F"),("rm_d","RM D")]


class PmpUpdatedForm(forms.Form):

    pmp   = forms.ChoiceField(label="PMP", choices=pmps)

    type = forms.ChoiceField(label="Type", choices=types)

    # type = forms.ModelChoiceField(label="Type", queryset=Route.objects.all())

    region = forms.ModelChoiceField(label=("Select Region"), queryset=Region.objects.all())





from django import forms
from  master_files.models import Region, Route, Address
from bootstrap_datepicker.widgets import DatePicker

class DistBibleForm(forms.Form):

    dist   = forms.ModelChoiceField(label=("Distributor"), queryset=Address.objects.filter(typ__name="lbm_contractor"))

    date = forms.DateField(widget=DatePicker(options={"format": "mm/dd/yyyy", "autoclose": True, "todayHighlight": True}), required=False)

    homeno = forms.BooleanField(label=("Home No"), required=False)

    mobileno = forms.BooleanField(label=("Mobile No"), required=False)

    emailno = forms.BooleanField(label=("E-mail Address"), required=False)



from bootstrap_datepicker.widgets import DatePicker
from  master_files.models import Region

Choice = Region.objects.all()

class RegionBibleForm(forms.Form):

    region   = forms.ModelChoiceField(label=("Select Region"), queryset=Region.objects.all() )

    date     = forms.DateField(widget=DatePicker(options={"format": "mm/dd/yyyy","autoclose": True}),  required=False)

    homeno   = forms.BooleanField(label=("Home No"), required=False)

    mobileno   = forms.BooleanField(label=("Mobile No"),  required=False)




from bootstrap_datepicker.widgets import DatePicker

class AddressDetails(forms.Form):

    distrib = forms.ModelChoiceField(label=("Distributor"), queryset=Address.objects.filter(typ__name="lbm_contractor"))

    date = forms.DateField(widget=DatePicker(options={"format": "mm/dd/yyyy", "autoclose": True}), required=False)

    isc  = forms.BooleanField(label=("Is Current"), required=False)

    distb = forms.BooleanField(label=("Distributor"), required=False)

    sdistb = forms.BooleanField(label=("Sub Distributor"), required=False)

    contrc = forms.BooleanField(label=("Contractor"), required=False)

    hacontrc = forms.BooleanField(label=("Has Agency Contract"), required=False)

    hccontrc = forms.BooleanField(label=("Has Coural Contract"), required=False)




from django import forms
from  master_files.models import Region, Route, Address
from bootstrap_datepicker.widgets import DatePicker

pmps  = [("1","with PMP"),("2","without PMP"),("3","Descriptions without PMP"),("4","Area Totals")]
types = [("num_total","Total"),("num_farmers","Farmers"),("num_lifestyle","Life Style"),("num_diaries","Diary"),("num_sheep","Sheep"),("num_beef","Beef"),
         ("num_sheepbeef","Sheep Beef"),("num_diarybeef","Diary Beef"),("num_hort","Hort"),("num_nzfw","Fat@90%"),("rmt","RMT"),("rm_rr","RM RR"),("rm_f","RM F"),("rm_d","RM D")]


class DistPmpUpdatedForm(forms.Form):

    pmp   = forms.ChoiceField(label="PMP", choices=pmps)

    type = forms.ChoiceField(label="Type", choices=types)

    dbutor = forms.ModelChoiceField(label=("Distributor"), queryset=Address.objects.filter(typ__name="lbm_contractor"))

    region = forms.ModelChoiceField(label=("Select Region"), queryset=Region.objects.all())

