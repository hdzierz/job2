from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import *

################# MAINTENANCE ######################


class ReportView(View):
    template_name = 'page_report.html'
    form_class = None


class MonthlyJobReport(ReportView):
    form_class = MonthyJobForm





