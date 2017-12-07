from django import forms
from .models import *

island_choices = [("NI","NI"), ("SI","SI"), ("ALL","ALL")]
region_choices = [("ALL","ALL")]
area_choices = [("ALL","ALL")]
rd_choices = [("ALL","ALL")]
cont_choices = [("","")]

class LbmJobRouteForm(forms.Form):
    #reg = forms.ModelMultipleChoiceField(label="R", queryset=Island.objects.all())
    island = forms.ChoiceField(label="Island", choices=island_choices)
    region = forms.MultipleChoiceField(label="Region", choices=region_choices)
    area = forms.MultipleChoiceField(label="Area", choices=area_choices)
    rd = forms.MultipleChoiceField(label="RD", choices=rd_choices)
    version = forms.IntegerField()
    inc_zero = forms.BooleanField(required=False)
    bdl_contractors = forms.ChoiceField(label="Contractor", choices=cont_choices)
    bdl_qty = forms.IntegerField()
    bdl_price = forms.FloatField()


choices = [("","")]

#clients = Client.objects.all().order_by('name')
#for client in clients:
#    opt = (client.name, client.name)
#    choices.append(opt)

job_choices = [("","")]
#jobs = Job.objects.filter(finished='N').order_by('-job_no')
#for job in jobs:
#    job_choices.append((job.job_no, job.job_no))

pub_choices = [("","")]
#pubs = Job.objects.values('publication').distinct().order_by('publication')
#for pub in pubs:
#    pub_choices.append((pub['publication'],pub['publication']))

class JobForm(forms.Form):
    publication = forms.ChoiceField(label="Publication", choices=pub_choices)
    client = forms.ChoiceField(label="Client", choices=choices)
    job_no = forms.ChoiceField(label="JobNo", choices=job_choices)
    frm = forms.CharField(label="From")
    to = forms.CharField(label="To")

    publication.widget.attrs['class'] = 'form-control select2'
    client.widget.attrs['class'] = 'form-control select2'
    job_no.widget.attrs['class'] = 'form-control select2'
    frm.widget.attrs['class'] = 'form-control'
    to.widget.attrs['class'] = 'form-control'


from django.forms import Select

class JobBookForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            #if self.fields[field].required:
            #    self.fields[field].widget.attrs.update({'aria-required': 'true'})
            #else:
            self.fields[field].widget.attrs.update({'required': 'false'})

            att = "form-control "
            if(isinstance(self.fields[field].widget, Select)):
                att += "select2 "

            if("date" in field):
                att += "basic-datepicker " 

            if("comment" in field):
                att += "icon-textarea"

            self.fields[field].widget.attrs.update({
                'class': att
            })

            if("rate" in field or "fee" in field):
                self.fields[field].widget.attrs.update({
                    'placeholder': "0.0000"
                })
    

    class Meta:
        model = LBMJob
        fields = '__all__'
