from django.shortcuts import render
from django.views import View
from lbm.models import LBMJob
from .tables import *
from .forms import *
from django.db.models import Q
		
# LBM -------
def page_invoice(request):
    jobs = LBMJob.objects.filter(Q(finished='N') & (Q(cancelled='N') | Q(cancelled='')))
	
    invoice_nos = [int(job.invoice_no[1:]) for job in jobs if job.invoice_no != '']
    start_invoice_number = max(invoice_nos) + 1
    
    if request.method == 'POST':
        if 'create_invoices' in request.POST:
            invoice_date = datetime.strptime(request.POST.get('invoice_date'), '%m/%d/%Y')
			
            job_ids = request.POST.getlist('invoice_selection[]')
            for job_id in job_ids:
                job = jobs.get(pk=job_id)
                if job.invoice_no == '':
                    job.invoice_no = 'C' + str(start_invoice_number)
                    job.invoice_date = invoice_date.strftime('%Y-%m-%d')
                    start_invoice_number += 1
					
                    job.save()
			
            jobs = LBMJob.objects.filter(Q(finished='N') & (Q(cancelled='N') | Q(cancelled='')))
            form = InvoiceForm(initial={'start_number': start_invoice_number})
        elif 'close_jobs' in request.POST:
            job_ids = request.POST.getlist('invoice_selection[]')
            for job_id in job_ids:
                job = jobs.get(pk=job_id)
                job.finished = 'Y'
                job.save()
            
            jobs = LBMJob.objects.filter(Q(finished='N') & (Q(cancelled='N') | Q(cancelled='')))
            form = InvoiceForm(initial={'start_number': start_invoice_number})
        else:
            filtered = False

            start_number=request.POST.get('start_number')
            frm=datetime.strptime(request.POST.get('frm'), '%m/%d/%Y')
            to=datetime.strptime(request.POST.get('to'), '%m/%d/%Y')
			
            filtered=True
            jobs = jobs.filter(invoice_date__range=(frm, to))
            jobs = [job for job in jobs if int(job.invoice_no[1:]) > int(start_number)]
			
            if(not filtered):
                jobs = jobs[:20]

            if form.is_valid():
                pass
				
            form = InvoiceForm(request.POST)
    else:
        invoice_nos = [int(job.invoice_no[1:]) for job in jobs if job.invoice_no != '']
        form = InvoiceForm(initial={'start_number': start_invoice_number})

    table = InvoiceTable(jobs)
    invoice_creation_form = InvoiceCreationForm();
    page_name = "invoice"

    return render(request, 'page_invoice.html', {'invoice_creation_form': invoice_creation_form, 'form': form, 'table':table, 'page_name':page_name})

