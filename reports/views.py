from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db.models import Q
from django.shortcuts import render
from django.views import View

from .forms import *


class ReportView(View):
    template_name = 'page_reports.html'
    cols = []
    
    search_field_conf = {
        'targets': ['name'],
        'query_method': 'icontains',
        }

    form_class = None
    model = None
    data = None
    form = None
    ajax = False
    report = "unknown"
    header = "none"


    def get(self, request):
        if self.form_class and request.GET.get('report'):
            self.form = self.form_class(request.GET)
            if self.form.is_valid():
                data = self.result(request)
                msg = ""
            else:
                data = []
                msg = "Please verify form input"
        else:
            self.form = self.form_class()
            data = self.result(request)
            msg = "No report"

        return render(request, self.template_name, 
                {
                    'report': self.report,
                    'header': self.header,
                    'msg': msg, 
                    'form': self.form,
                    'model': self.model,
                    'data': data,
                    'cols': self.cols,
                    'ajax': self.ajax,
                }
            )

    def result(self, request):
        return []

    def post(self, request):
        res = []
        if self.ajax:
            draw = request.POST.get('draw')
            start = int(request.POST.get('start'))
            length = int(request.POST.get('length'))
            search = request.POST.get('search[value]')
            regex = request.POST.get('search[regex]')
            order_col = request.POST.get('order[0][column]')
            order_dir = request.POST.get('order[0][dir]')

            o_col = self.cols[int(order_col)]

            if(order_dir == "desc"):
                o_col = '-' + o_col.lower()

            o_col = o_col.lower()
    
            query_method = self.search_field_conf['query_method']
            filt_cols = self.search_field_conf['targets']

            if(regex != 'false'):
                query_method="iregex"

            q_and = Q(pk__gt=0)

            if(search != ''):
                search_apl = search.split(';')
                for s in search_apl:
                    q = Q(pk=-1)
                    for f in filt_cols:
                        kwargs = {'{0}__{1}'.format(f, query_method): s}
                        q = q | Q(**kwargs)
                    q_and = q_and & q

            i = 0
            has_col_search = False
            for c in self.cols:
                col_str = 'columns[' + str(i)  + '][search][value]'
                if col_str in request.POST:
                    val = request.POST.get(col_str)
                    if val != '':
                        kwargs = {'{0}__{1}'.format(col, query_method): val}
                        q_and = q_and & Q(**kwargs)
                        has_col_search = True
                i += 1

            if(search!='' or has_col_search):
                routes = cls.objects.filter(q_and).order_by(o_col)
                ct_filtered = routes.count()
                routes = routes[start:(start+length)]
            else:
                routes = cls.objects.all().order_by(o_col)[start:(start+length)]
                ct_filtered = cls.objects.all().count()

            data = []
            for r in routes:
                d = []
                for c in cols:
                    d.append(str(getattr(r,c.lower())))
                data.append(d)

            res = {}
            res['draw'] = draw
            res['data'] = data
            res['recordsTotal'] = int(cls.objects.all().count())
            res['recordsFiltered'] = ct_filtered

        return JsonResponse(res)


from lbm.models import LBMJob, LBMJobRoute
from django.forms.models import model_to_dict
from django.db.models import Sum
import datetime

class MonthlyJobReport(ReportView):
    form_class = MonthlyJobForm
    cols = ["job__job_no", "job__delivery_date","amount__sum",]

    def result(self, request):
        month = request.GET.get('month')
        year = request.GET.get('year')

        dtt_str = str(year) + '-' + str(month)
   
        month = '6'
        year = '2016'
        dtt = datetime.date(2012,2,14)

        sel = ["job__job_no", "job__delivery_date", ]
        jobs = LBMJobRoute.objects.filter(job__delivery_date=dtt).values(*sel).annotate(Sum('amount'))

        #res = []

        #for job in jobs:
           #res.append(model_to_dict(job, fields=self.cols))

        return jobs



class WeeklyReport(ReportView):
    form_class = MonthlyJobForm
    cols = ["job__job_no", 
            "job__is_regular", 
            "job__dest_type", 
            "job__publication", 
            "job__delivery_date",
            "dropoff__company",
            "route__code", 
            "amount__sum",]
    
    def result(self, request):
        month = request.GET.get('month')
        year = request.GET.get('year')

        dtt_str = str(year) + '-' + str(month)
   
        dtt = datetime.date(2012,2,14)

        sel = self.cols[:]
        del sel[-1]

        jobs = LBMJobRoute.objects.filter(job__delivery_date=dtt).values(*sel).annotate(Sum('amount'))

        return jobs
  

class SummaryDeliveryInstructions(ReportView):
    form_class = SummaryDeliveryInstructionsForm
    cols = ["job__job_no", 
            "job__is_regular", 
            "job__dest_type__name", 
            "job__publication__name", 
            "job__delivery_date",
            "dropoff__last_name",
            "amount",
    ]
	
    def result(self, request):
        frm = request.GET.get('from')
        to = request.GET.get('to')
        dist = request.GET.get('dist')

        sel = self.cols[:]
        del sel[-1]
        self.cols.append("amount__sum")

        if dist:
            crit1 = Q(job__delivery_date__gt=frm)
            crit2 = Q(job__delivery_date__lt=to)
            crit3 = Q(dist__id=dist)
            jobs = LBMJobRoute.objects.filter(
                crit1 & crit2 & crit3,
                ).values(*sel).annotate(Sum('amount'))
        else:
            jobs = LBMJobRoute.objects.filter(job__job_no__gt=80000).values(*sel).annotate(Sum('amount'))

        return jobs


from django.forms.models import model_to_dict
import time

class PmpUpdated(ReportView):
    form_class = PmpUpdatedForm
    template_name = 'page_reports.html'

    report = "PMP Updated"
    header = "RURAL DELIVERY NUMBERS " + str(datetime.date.today()) 
    cols = ['route__rd','route__pmp_areacode' ,'route__pmp_runcode','route__region__name', 'route__total',]

    def result(self, request):
        pmp = request.GET.get('pmp')
        typ = request.GET.get('type')
        region = request.GET.get('region')

        if typ != None:
            buff = CfgJobType.objects.get(id=typ)
            self.cols[-1] = 'route__' + buff.name.lower()
      
        return RouteAff.objects.filter(
                route__region__id=region,
                app_date__lt=datetime.datetime.now()
                ).order_by('-app_date')[:1].values(*self.cols)


class AddressDetails(ReportView):
    form_class = AddressDetails
    template_name = 'page_reports_archived_addressDetails.html'
    cols = ['first_name','last_name','address']

    def result(self, request):
        dist = request.GET.get('dist')
        date = request.GET.get('date')

        sel = ['first_name','last_name','address']

        addres = Address.objects.filter(typ__name=dist).values(*sel)

        return addres


class DistBible(ReportView):
    form_class = DistBibleForm
    template_name = 'page_reports_archived_distBible.html'
    cols = ['first_name','last_name','address']

    def result(self, request):
        dist = request.GET.get('dist')
        date = request.GET.get('date')
        homeno = request.GET.get('homeno')
        mobileno = request.GET.get('mobileno')
        emailno = request.GET.get('email')

        sel = ['first_name','last_name','address']


        dists = Address.objects.filter(typ__name=dist).values(*sel)

        return dists


from django.forms.models import model_to_dict

class RegionBible(ReportView):
    form_class = RegionBibleForm
    template_name = 'page_reports_archived_regionBible.html'
    cols = ['route__code', 'pcl_dropoff__first_name', 'lbm_dropoff__last_name', 'lbm_dropoff__phone',
            'lbm_dropoff__address', 'route__description']


    def result(self, request):
        region = request.GET.get('region')
        date = request.GET.get('date')
        homephone = request.GET.get('homeno')
        mobilephone = request.GET.get('mobileno')


        sel = ['route__code', 'pcl_dropoff__first_name', 'lbm_dropoff__last_name', 'lbm_dropoff__phone',
               'lbm_dropoff__address', 'route__description']

        routes = RouteAff.objects.filter(route__region__id=region).values(*sel)

        return routes


import time

class DistPmpUpdated(ReportView):
    form_class = DistPmpUpdatedForm
    template_name = 'page_reports.html'

    report = "PMP Updated by Distributor"
    header = "RURAL DELIVERY NUMBERS " + str(datetime.date.today())
    cols = ['route__rd', 'route__pmp_areacode', 'route__pmp_runcode', 'route__region__name', 'lbm_dist__company', 'route_total']

    def result(self, request):
        dbutor = request.GET.get('dbutor')
        pmp = request.GET.get('pmp')
        typ = request.GET.get('type')

        if typ != None:
            buff = CfgJobType.objects.get(id=typ)
            self.cols[-1] = 'route__' + buff.name.lower()

        return RouteAff.objects.filter(
                lbm_dist__id=dbutor,
                app_date__lt=datetime.datetime.now()
                ).order_by('-app_date')[:1].values(*self.cols)


dist_cols = ["job__job_no","job__is_regular","job__publication__name", "job__client__company", "job__dest_type__name", "job__delivery_date", "dropoff__company", "amount__sum", ]

from django.template import Context, Template
from django.template.loader import get_template
from wkhtmltopdf.views import PDFTemplateView, PDFTemplateResponse
import pdfkit

def bible_send(request):
    dist_t = get_template("pdf_deliv_dist.html")

    dists = Address.objects.filter(typ__name="lbm_dist")
    for dist in dists:
        print("Processing " + dist.company)
        sel = dist_cols[:]
        del sel[-1]
        vals = LBMJobRoute.objects.filter(dist=dist).values(*sel).annotate(Sum('amount')).order_by("job__publication__name")
        c = {"cols":dist_cols, "data":vals, "dist": dist.company}
        html = dist_t.render(c)
        pdfkit.from_string(html, "delivery/" + dist.company + '.pdf')

    return HttpResponse("test")

#        return PDFTemplateResponse(request=request,
#			template=dist_t,
#                        filename="hello.pdf",
#                        context= c,
#                        show_content_in_browser=False,
#                        cmd_options={'margin-top': 50,},
#                         )


from wkhtmltopdf.views import PDFTemplateView, PDFResponse


class MyPDF(PDFTemplateView):
    filename = 'my_pdf.pdf'
    template_name = 'page_reports.html'
    cmd_options = {
        'margin-top': 3,
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tt'] = 'test'
        return context



