from django.shortcuts import render
from django.core import serializers
from django.views.generic import ListView
from .models import *
from .tables import *
from django.http import JsonResponse
from django.forms.models import model_to_dict

from django.views.generic.edit import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.contrib.auth.models import User, Group
from django.db.models import Q


class RouteAffCreate(CreateView):
    model = RouteAff
    fields = '__all__'
    template_name = 'master_files_route_form.html'
    success_url = '/master_files/config/'

    def page_name(self):
        return "Create Route Affiliation"

    def btn(self):
        return "Create"


class RouteAffUpdate(UpdateView):
    model = RouteAff
    fields = '__all__'
    template_name = 'master_files_route_form.html'
    success_url = '/master_files/config/'

    def page_name(self):
        return "Update Route Affiliation"

    def btn(self):
        return "Update"


class RouteAffDelete(DeleteView):
    model = RouteAff
    fields = '_all__'
    template_name = 'master_files_route_form.html'
    success_url = '/master_files/address/'

    def page_name(self):
        return "Delete Route Affiliation"

    def btn(self):
        return "Delete"



class ConfigCreate(CreateView):
    model = Config
    fields = '__all__'
    template_name = 'master_files_route_form.html'
    success_url = '/master_files/config/'

    def page_name(self):
        return "Create Config"

    def btn(self):
        return "Create"


class ConfigUpdate(UpdateView):
    model = Config
    fields = '__all__'
    template_name = 'master_files_route_form.html'
    success_url = '/master_files/config/'

    def page_name(self):
        return "Update Config"

    def btn(self):
        return "Update"



class UserCreate(CreateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'groups',
           'is_staff', 'is_active', ]
    template_name = 'master_files_route_form.html'
    success_url = '/master_files/user/'

    def page_name(self):
        return "Create User"

    def btn(self):
        return "Create"


class UserUpdate(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'groups',
           'is_staff', 'is_active', 'password']
    template_name = 'master_files_route_form.html'
    success_url = '/master_files/user/'

    def page_name(self):
        return "Update User"

    def btn(self):
        return "Update"



class AddressCreate(CreateView):
    model = Address
    fields = '__all__'
    template_name = 'master_files_address_form.html'
    success_url = '/master_files/address/'

    def page_name(self):
        return  'Create Address'

    def btn(self):
        return "Create"


class AddressUpdate(UpdateView):
    model = Address
    fields = '__all__'
    template_name = 'master_files_address_form.html'
    success_url = '/master_files/address/'

    def page_name(self):
        return  'Update Address'

    def btn(self):
        return "Update"


class AddressDelete(DeleteView):
    model = Address
    fields = '_all__'
    template_name = 'master_files_address_form.html'
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
        
        if(regex != 'false'):
            query_method="iregex"

        print(request.GET.dict())

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
        for c in cols:
            col_str = 'columns[' + str(i)  + '][search][value]'
            print(col_str)
            try:
                col = spec_order[c]
            except:
                col = c
            if col_str in request.GET:
                val = request.GET.get(col_str)
                print("h:" + val)
                if val != '':
                    kwargs = {'{0}__{1}'.format(col, query_method): val}
                    q_and = q_and & Q(**kwargs)
                    has_col_search = True
            i += 1
        print(q_and)

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
    

def ajax_data_table(request, model):
    if(model == "route"):
        cols = ["pk", "island", "region", "area", "code", "description", ]
        spec_order = {'island': 'island__name', "region": 'region__name', "area": "area__name"}
        m = Route
        filt_cols = ["code", "description", "region__name", "area__name"]
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
        cols = ["pk", "typ", "first_name", "last_name", ]
        spec_order = {"typ": "typ__name", }
        m = Address
        filt_cols = ["last_name"]
    elif(model == "user"):
        cols = ["pk", "username", "last_name", "groups", "email", ]
        spec_order = {"groups" : "groups__name"}
        m = User 
        filt_cols = ["username"]
    elif(model == 'config'):
        cols = ["pk", "name", "value"]
        m = Config
        spec_order = []
        filt_cols = ["name"]
    elif(model == 'route_aff'):
        cols = ["pk", "address", "route", "app_date", ]
        m = RouteAff
        spec_order = ["route__code", "address_company",]
        filt_cols = ["address", "route"]

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
        cols = ["pk", "typ", "first_name", "last_name", ]
        sort_col = 3
    elif(model == "user"):
        cols = ["pk", "username", "last_name", "email", ]
        sort_col = 1
    elif(model == 'config'):
        cols = ["pk", "name", "value"]
        sort_col = 1
    elif(model == 'route_aff'):
        cols = ["pk", "address", "route", "app_date",]
        sort_col = 1
    

    return render(request, 'data_table.html', {'ajax':True, 'sort_col': sort_col, 'cols': cols, "model": model})



