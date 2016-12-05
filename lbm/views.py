from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from .models import *
from .tables import *
from .forms import *

from django.views.generic.edit import *

import logging


# Create your views here.

# Home ---------
def page_home(request):
    page_name = 'home'
    return render(request, 'index.html', {'page_name':page_name})


# Reports ---------
def page_reports_lbm_jobDetails(request):
    page_name = 'jobDetails'
    return render(request, 'page_reports_lbm_jobDetails.html', {'page_name':page_name})


class LBMJobView(FormView):
    form_class = JobBookForm 
    template_name = 'page_lbm_jobBooking.html'
    success_url = '/lbm/jobsCurrent/'

    def form_valid(self, form):
        return super(LBMJobView, self).form_valid(form)

    def page_name(self):
        return "LBM Job Booking"

    def btn(self):
        return "Update"


# LBM ROUTES

def page_lbm_jobRoutes(request, job_id):
    job = LBMJob.objects.get(pk=job_id)

    if request.method == 'POST':

        form = LbmJobRouteForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = LbmJobRouteForm(request.POST)

    routes = Route.objects.filter(job=job)
    table = RouteTable(routes)

    page_name = "lbm_routes"
    return render(request, 'page_lbm_job_routes.html', {'job':job, 
        'page_name':page_name,
        'form':form,
        'table':table})


# LBM -------
def page_lbm(request):
    if request.method == 'POST':
        filtered = False
        jobs = LBMJob.objects.filter(finished='N')
        #if(request.GET.get('frm'):
        #    jobs.filter()
        #if(request.GET.get('frm'):
        #    jobs.filter()

        publication=request.POST.get('publication')
        #if(publication):
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
        jobs = LBMJob.objects.filter(finished='N')[:20]
        table = JobTable(jobs)

    page_name = "lbm"

    return render(request, 'page_test.html', {'form': form, 'table':table, 'page_name':page_name})

