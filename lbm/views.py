from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from .models import *
from .tables import *
from .forms import *
import logging


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

# Test -------
def page_test(request):
    logging.debug('TT: ' + request.method)
    if request.method == 'POST':
        filtered = False
        jobs = Job.objects.filter(finished='N')
        #if(request.GET.get('frm'):
        #    jobs.filter()
        #if(request.GET.get('frm'):
        #    jobs.filter()

        publication=request.POST.get('publication')
        #if(publication):
        logging.debug("Hello")
        filtered=True
        jobs = jobs.filter(publication=publication)
        #if(request.GET.get('frm'):
        #             jobs.filter()
        #if(request.GET.get('frm'):
        #            jobs.filter()
        if(not filtered):
            jobs = jobs[:20]
        table = JobTable(jobs)

        form = JobForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = JobForm()
        jobs = Job.objects.filter(finished='N')[:20]
        table = JobTable(jobs)

    return render(request, 'page_test.html', {'form': form, 'table':table})

