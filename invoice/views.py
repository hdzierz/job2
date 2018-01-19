from django.shortcuts import render
from django.views import View
from lbm.models import LBMJob
from .tables import *
from django.db.models import Q
		
# LBM -------
def page_invoice(request):
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
        form = None
        jobs = LBMJob.objects.filter(Q(finished='N') & (Q(cancelled='N') | Q(cancelled='')))
        table = InvoiceTable(jobs)

    page_name = "invoice"

    return render(request, 'page_invoice.html', {'form': form, 'table':table, 'page_name':page_name})

