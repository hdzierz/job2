from master_files.models import *
from django import forms
from bootstrap_datepicker.widgets import DatePicker

class MonthlyJobForm(forms.Form):
    month = forms.CharField(label='Your name', max_length=100)
    year = forms.CharField(label='Your name', max_length=100) 



class SummaryDeliveryInstructionsForm(forms.Form):
    frm = forms.DateField(widget=DatePicker(options={"format": "mm/dd/yyyy", "autoclose": True}), label='Start Date')
    to = forms.DateField(widget=DatePicker(options={"format": "mm/dd/yyyy", "autoclose": True}), label="Final Date")
    dist = forms.ModelChoiceField(\
            queryset=Address.objects.filter(typ__name="lbm_dist")
            )
    comment = forms.CharField(label="Comment")


class SummaryDeliveryInstructionsJobForm(forms.Form):
    frmj = forms.DateField(widget=DatePicker(options={"format": "mm/dd/yyyy", "autoclose": True}), label='Start Date')
    toj = forms.DateField(widget=DatePicker(options={"format": "mm/dd/yyyy", "autoclose": True}), label="Final Date")
    commentj = forms.CharField(label="Comment")




pmps  = [("1","with PMP"),("2","without PMP"),("3","Descriptions without PMP"),("4","Area Totals")]

class PmpUpdatedForm(forms.Form):
    pmp   = forms.ChoiceField(label="PMP", choices=pmps)
    type = forms.ModelChoiceField(label="Type", queryset=CfgJobType.objects.exclude(name="bundles").order_by('name'))
    region = forms.ModelChoiceField(label=("Select Region"), queryset=Region.objects.all())


class DistBibleForm(forms.Form):
    dist   = forms.ModelChoiceField(label=("Distributor"), queryset=Address.objects.filter(typ__name="lbm_contractor"))
    date = forms.DateField(widget=DatePicker(options={"format": "mm/dd/yyyy", "autoclose": True, "todayHighlight": True}), required=False)
    homeno = forms.BooleanField(label=("Home No"), required=False)
    mobileno = forms.BooleanField(label=("Mobile No"), required=False)
    emailno = forms.BooleanField(label=("E-mail Address"), required=False)


class RegionBibleForm(forms.Form):
    region   = forms.ModelChoiceField(label=("Select Region"), queryset=Region.objects.all() )
    date     = forms.DateField(widget=DatePicker(options={"format": "mm/dd/yyyy","autoclose": True}),  required=False)
    homeno   = forms.BooleanField(label=("Home No"), required=False)
    mobileno   = forms.BooleanField(label=("Mobile No"),  required=False)


class AddressDetails(forms.Form):


    distrib = forms.ModelChoiceField(label=("Distributor"), queryset=Address.objects.filter(typ__name="lbm_contractor"))
    date = forms.DateField(widget=DatePicker(options={"format": "mm/dd/yyyy", "autoclose": True}), required=False)
    isc  = forms.BooleanField(label=("Is Current"), required=False)
    distb = forms.BooleanField(label=("Distributor"), required=False)
    sdistb = forms.BooleanField(label=("Sub Distributor"), required=False)
    contrc = forms.BooleanField(label=("Contractor"), required=False)
    hacontrc = forms.BooleanField(label=("Has Agency Contract"), required=False)
    hccontrc = forms.BooleanField(label=("Has Coural Contract"), required=False)


pmps  = [("1","with PMP"),("2","without PMP"),("3","Descriptions without PMP"),("4","Area Totals")]

class DistPmpUpdatedForm(forms.Form):
    pmp   = forms.ChoiceField(label="PMP", choices=pmps)
    type = forms.ModelChoiceField(label="Type", queryset=CfgJobType.objects.all().order_by('name'))

    dbutor = forms.ModelChoiceField(label=("Distributor"),  queryset=Address.objects.filter(typ__name="lbm_contractor"))


