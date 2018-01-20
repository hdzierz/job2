from django.shortcuts import render
from django.views import View
from lbm.models import LBMJob
from .tables import *
from .forms import *
from django.db.models import Q
		
# LBM -------
def page_invoice(request):
    if request.method == 'POST':
        filtered = False
        jobs = LBMJob.objects.filter(Q(finished='N') & (Q(cancelled='N') | Q(cancelled='')))
        #if(request.GET.get('frm'):
        #    jobs.filter()
        #if(request.GET.get('frm'):
        #    jobs.filter()

        start_number=request.POST.get('start_number')
        frm=datetime.strptime(request.POST.get('frm'), '%m/%d/%Y')
        to=datetime.strptime(request.POST.get('to'), '%m/%d/%Y')
        #if(publication):
        filtered=True
        jobs = jobs.filter(invoice_date__range=(frm, to))
        jobs = [job for job in jobs if job.invoice_no!= '']
        jobs = [job for job in jobs if int(job.invoice_no[1:]) > int(start_number)]
        #if(request.GET.get('frm'):
        #             jobs.filter()
        #if(request.GET.get('frm'):
        #            jobs.filter()
        if(not filtered):
            jobs = jobs[:20]
        table = InvoiceTable(jobs)

        form = InvoiceForm(request.POST)
        if form.is_valid():
            pass
    else:
        jobs = LBMJob.objects.filter(Q(finished='N') & (Q(cancelled='N') | Q(cancelled='')))
        invoice_nos = [int(job.invoice_no[1:]) for job in jobs if job.invoice_no != '']
        form = InvoiceForm(initial={'start_number': max(invoice_nos) + 1})
        jobs = [job for job in jobs if job.invoice_no!= '']
        table = InvoiceTable(jobs)

    page_name = "invoice"

    return render(request, 'page_invoice.html', {'form': form, 'table':table, 'page_name':page_name})

