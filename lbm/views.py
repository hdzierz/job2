from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, JsonResponse
from .models import *
from .tables import *
from .forms import *

from django.views.generic.edit import *

import logging

# Create your views here.

def api_get_regions(request, tgt, search):
    cls = eval(tgt)

    if(search == "ALL"):
        buff = cls.objects.all()
    else:
        search = search.split(',')
        if(tgt == "Region"):
            buff = cls.objects.filter(island__name__in=search)
        elif(tgt == "Area"):
            buff = cls.objects.filter(region__name__in=search)
        elif(tgt == "Route"):
            buff = cls.objects.filter(area__name__in=search)
    
    res = {}
    for r in buff:
        if tgt=="Route":
            res[str(r.pk)] = r.code
        else:
            res[str(r.pk)] = r.name

    return JsonResponse(res)


# Home ---------
def page_home(request):
    page_name = 'home'
    return render(request, 'index.html', {'page_name':page_name})


# Reports ---------
def page_reports_lbm_jobDetails(request):
    page_name = 'jobDetails'
    return render(request, 'page_reports_lbm_jobDetails.html', {'page_name':page_name})


# This is a view that shows a single job
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


def page_lbm_jobBooking(request, job_id=None):
    if(job_id):
        job = LBMJob.objects.get(pk=job_id)
    else:
        job = LBMJob()   

    if request.method=="POST":
        form = JobBookForm(request.POST)
        if(form.is_valid()):
            form.save()
    else:
        form = JobBookForm(instance=job)
         
    return render(request, 'page_lbm_jobBooking.html', {"job": job, "form": form})


# LBM ROUTES

def page_lbm_jobRoutes(request, job_id):
    job = LBMJob.objects.get(pk=job_id)

    if request.method == 'POST':

        form = LbmJobRouteForm(request.POST)
        #if form.is_valid():
        rds = request.POST.getlist('rd')
        for rd in rds:
            route = Route.objects.get(pk=int(rd))
            ra = RouteAff.GetLBMContractor(route)
            jr = LBMJobRoute()
            jr.route = route
            jr.job = job
            jr.dest_type = job.dest_type
            jr.dist = ra.lbm_dist
            jr.subdist = ra.lbm_subdist
            jr.contractor = ra.lbm_contractor
            jr.dropoff = ra.lbm_dropoff
            jr.save()
    
    else:
        form = LbmJobRouteForm()

    routes = LBMJobRoute.objects.filter(job=job)
    table = JobRouteTable(routes)

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
        table = JobTable(jobs.order_by("-last_name"))

        form = JobForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = JobForm()
        jobs = LBMJob.objects.filter(finished='N')[:20]
        table = JobTable(jobs)

    page_name = "lbm"

    return render(request, 'page_test.html', {'form': form, 'table':table, 'page_name':page_name})

