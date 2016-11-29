from django.shortcuts import render
from django.core import serializers
from django.views.generic import ListView
from lbm.models import Route
from .tables import *
from django.http import JsonResponse
from django.forms.models import model_to_dict

class DataTable:
    model = Route
    cols = []
    filt_cols = ["name"]
    query_method = 'icontains'

    def __init__(self):
        pass

    def render(self, request):
        pass


def data_table(request, cls=Route, cols=[], filt_cols=["code"], query_method='icontains'):
    if(request.method == "GET"):
        draw = request.GET.get('draw')
        start = int(request.GET.get('start'))
        length = int(request.GET.get('length'))
        search = request.GET.get('search[value]')
        regex = request.GET.get('search[regex]')

        if(regex):
            query_method="iregex"

        kwargs = {}
        for f in filt_cols:
            st = '{0}__{1}'.format(f, query_method) 
            kwargs[st] = search
            
        if(search):
            routes = cls.objects.filter(**kwargs)[start:(start+length)]
            ct_filtered = routes.count()
        else:
            routes = cls.objects.all()[start:(start+length)]
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
    

def page_data_table(request):
    cols = ["Island", "Region", "Area", "Code", "Description", ]
    return data_table(request, Route, cols)


def page_route_list(request):
    cols = ["Island", "Region", "Area", "Code", "Description", ]
    
    return render(request, 'data_table.html', {'cols': cols})


# Create your views here.
