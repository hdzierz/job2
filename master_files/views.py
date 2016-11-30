from django.shortcuts import render
from django.core import serializers
from django.views.generic import ListView
from .models import *
from .tables import *
from django.http import JsonResponse
from django.forms.models import model_to_dict

from django.views.generic.edit import *


class AddressCreate(CreateView):
    model = Address
    fields = '__all__'
    template_name = 'master_files_route_form.html'
    success_url = '/master_files/address/'

    def page_name(self):
        return  'Create Address'

    def btn(self):
        return "Create"


class AddressUpdate(UpdateView):
    model = Address
    fields = '__all__'
    template_name = 'master_files_route_form.html'
    success_url = '/master_files/address/'

    def page_name(self):
        return  'Update Address'

    def btn(self):
        return "Update"


class AddressDelete(DeleteView):
    model = Address
    fields = '_all__'
    template_name = 'master_files_route_form.html'
    success_url = '/master_files/address/'

    def page_name(self):
        return "Delete Address"

    def btn(self):
        return "Delete"


class RouteCreate(CreateView):
    model = Route
    fields = '__all__'
    template_name = 'master_files_route_form.html'
    success_url = '/master_files/route/'

    def page_name(self):
        return  'Create Route'

    def btn(self):
        return "Create"


class RouteUpdate(UpdateView):
    model = Route
    fields = '__all__'
    template_name = 'master_files_route_form.html'
    success_url = '/master_files/route/'

    def page_name(self):
        return  'Update Route'

    def btn(self):
        return "Update"


class RouteDelete(DeleteView):
    model = Route
    fields = '_all__'
    template_name = 'master_files_route_form.html'
    success_url = '/master_files/route/'

    def page_name(self):
        return "Delete Route"

    def btn(self):
        return "Delete"

    

class RegionCreate(CreateView):
    model = Region
    fields = '__all__'
    template_name = 'master_files_route_form.html'
    success_url = '/master_files/region/'

    def page_name(self):
        return  'Create Region'

    def btn(self):
        return "Create"


class RegionUpdate(UpdateView):
    model = Region
    fields = '__all__'
    template_name = 'master_files_route_form.html'
    success_url = '/master_files/region/'

    def page_name(self):
        return  'Update Region'

    def btn(self):
        return "Update"


class RegionDelete(DeleteView):
    model = Region
    fields = '_all__'
    template_name = 'master_files_route_form.html'
    success_url = '/master_files/region/'

    def page_name(self):
        return "Delete Region"

    def btn(self):
        return "Delete"



class AreaCreate(CreateView):
    model = Area
    fields = '__all__'
    template_name = 'master_files_route_form.html'
    success_url = '/master_files/area/'

    def page_name(self):
        return  'Create Area'

    def btn(self):
        return "Create"


class AreaUpdate(UpdateView):
    model = Area
    fields = '__all__'
    template_name = 'master_files_route_form.html'
    success_url = '/master_files/area/'

    def page_name(self):
        return  'Update Area'

    def btn(self):
        return "Update"


class AreaDelete(DeleteView):
    model = Area
    fields = '_all__'
    template_name = 'master_files_route_form.html'
    success_url = '/master_files/area/'

    def page_name(self):
        return "Delete Area"

    def btn(self):
        return "Delete"


class DataTable:
    model = Route
    cols = []
    filt_cols = ["name"]
    order_cols = None
    query_method = 'icontains'
    qs = None

    def __init__(self, qs):
        self.qs = qs

    def render(self, request):
        draw = request.GET.get('draw')
        start = int(request.GET.get('start'))
        length = int(request.GET.get('length'))
        search = request.GET.get('search[value]')
        regex = request.GET.get('search[regex]')
        order_col = request.GET.get('order[0][column]')
        order_dir = request.GET.get('order[0][dir]') 
        
        o_col = cols[int(order_col)]

        try:
            o_col = spec_order[o_col]
        except:
            pass

        if(order_dir == "desc"):
            o_col = '-' + o_col.lower()

        o_col = o_col.lower()

        if(regex):
            query_method="iregex"
        kwargs = {}
        for f in filt_cols:
            st = '{0}__{1}'.format(f, query_method)
            kwargs[st] = search

        if(search):
            routes = cls.objects.filter(**kwargs).order_by(o_col)[start:(start+length)]
            ct_filtered = routes.count()
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



def data_table(request, cls=Route, cols=[], filt_cols=["code"], query_method='icontains', spec_order={}):
    if(request.method == "GET"):
        draw = request.GET.get('draw')
        start = int(request.GET.get('start'))
        length = int(request.GET.get('length'))
        search = request.GET.get('search[value]')
        regex = request.GET.get('search[regex]')
        order_col = request.GET.get('order[0][column]')
        order_dir = request.GET.get('order[0][dir]')

        o_col = cols[int(order_col)]

        try:
            o_col = spec_order[o_col]
        except:
            pass

        if(order_dir == "desc"):
            o_col = '-' + o_col.lower()

        o_col = o_col.lower()
        
        if(regex):
            query_method="iregex"

        kwargs = {}
        for f in filt_cols:
            st = '{0}__{1}'.format(f, query_method) 
            kwargs[st] = search
            
        if(search):
            routes = cls.objects.filter(**kwargs).order_by(o_col)[start:(start+length)]
            ct_filtered = routes.count()
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
    

def ajax_data_table(request, model):
    if(model == "route"):
        cols = ["pk", "island", "region", "area", "code", "description", ]
        spec_order = {'island': 'island__name', "region": 'region__name', "area": "area__name"}
        m = Route
        filt_cols = ["code", "description"]
    elif(model == "region"):
        cols = ["pk", "name", ]
        spec_order = []
        m = Region
        filt_cols = ["name"]
    elif(model == "area"):
        cols = ["pk", "name", ]
        spec_order = []
        m = Area
        filt_cols = ["name"]
    elif(model == "address"):
        cols = ["pk", "user", "company", ]
        spec_order = {"user" : "user__last_name"}
        m = Address
        filt_cols = ["company"]


    return data_table(request, cls=m, cols=cols, filt_cols=filt_cols, spec_order=spec_order)


def page_list(request, model):
    if(model == "route"):
        cols = ["pk", "Island", "Region", "Area", "Code", "Description", ]
        sort_col = 3
    elif(model == "region"):
        cols = ["pk", "Name", ]
        sort_col = 1
    elif(model == "area"):
        cols = ["pk", "Name", ]
        sort_col = 1
    elif(model == "address"):
        cols = ["pk", "User", "Company", ]
        sort_col = 1

    return render(request, 'data_table.html', {'sort_col': sort_col, 'cols': cols, "model": model})



