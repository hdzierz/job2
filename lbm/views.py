from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

# Create your views here.

def page_lbm(request):
    return render(request, 'page_base.html') 

