from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from .models import *

# Create your views here.

def page_lbm(request):
    jobs = Job.objects.all()[:20]
    jobs_open = Job.objects.filter(finished='N').count() 
    return render(request, 'page_lbm.html', {"jobs" : jobs, "jobs_open": jobs_open}) 

