from django import forms
from .models import *

island_choices = [("NI","SI")]
region_choices = [("","")]
area_choices = [("","")]
rd_choices = [("","")]
cont_choices = [("","")]

class LbmJobRouteForm(forms.Form):
    island = forms.ChoiceField(label="Island", choices=island_choices)
    region = forms.ChoiceField(label="Region", choices=region_choices)
    area = forms.ChoiceField(label="Area", choices=area_choices)
    rd = forms.ChoiceField(label="RD", choices=rd_choices)
    version = forms.IntegerField()
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
