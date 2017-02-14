from django.shortcuts import render



class DataTable:
    qs = None

    def __init__(self, qs):
        self.qs = qs



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


# Create your views here.
