from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from .models import *

# Create your views here.

# Home ---------
def page_home(request):
    return render(request, 'index.html')

# LBM ---------
def page_lbm(request):
    jobs = Job.objects.all()[:20]
    jobs_open = Job.objects.filter(finished='N').count()
    return render(request, 'page_lbm.html', {"jobs" : jobs, "jobs_open": jobs_open}) 

def page_lbm_jobBooking(request):
    return render(request, 'page_lbm_jobBooking.html')

# Reports ---------
def page_reports_lbm_jobDetails(request):
    return render(request, 'page_reports_lbm_jobDetails.html')