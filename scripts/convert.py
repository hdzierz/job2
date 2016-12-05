from lbm.models import *
from coural_legacy.models import *


r_ignore = ["route_id"]
ignore = ["route_id", "island", "area", "region", "code_rd"]
a_ignore = ["client_id", "etext", "name", "name2", "salutation", "salutation2", "address_id", "user", "operator_id","branch_id"]
j_ignore = ["is_quote", "job_id", "client_id", 'publication', ]
jr_ignore = ["concoll", "job_route_id", "job_id", "route_id", "dist_id", "contractor_id", "subdist_id",
"dropoff_id", "doff", ]


def conv_boolean(value):
    if value is None:
        return False
    elif isinstance(value, int):
        if(value==1):
                return True
        else:
                return False
    elif isinstance(value, str):
        if(value == 'Y'):
                return True
        else:
                return False
    else:
        return False


def update(c, nc, ignore):
    for f in c._meta.get_fields():
        print(f.name)
        fnlc = f.name
        if(fnlc not in ignore):
            val = getattr(c, fnlc)
            try:
                typ = nc._meta.get_field(fnlc).get_internal_type()
                if(typ == "BooleanField"):
                    val = conv_boolean(val)
            except:
                pass
            try:         
                setattr(nc, f.name, val)
            except:
                pass

c_master = False
c_lbm = True

def run():
    u = User.objects.get(username='hdzierz')

    if c_master:
        Route.objects.all().delete()
        for c in LCRoute.objects.all():
            nc = Route()
            update(c, nc, ignore)
            island, created = Island.objects.get_or_create(name=c.island)
            nc.island = island
            area, created = Area.objects.get_or_create(name=c.area)
            nc.area = area
            region, created = Region.objects.get_or_create(name=c.region)
            nc.region=region
            nc.rd = c.code
            nc.old_id = c.route_id
            nc.save()

        Address.objects.all().delete()
        for a in LCAddress.objects.all():
            na = Address()
            na.old_id = a.address_id
            na.old_operator_id = a.operator_id
            na.old_client_id = a.client_id
            update(a, na, a_ignore)
            na.last_name = a.name
            na.last_name2 = a.name2
            if(na.email is None):
                na.email = "howard@coural.co.nz"
            na.save() 

        for c in LCClient.objects.all():
            na = Address()
            na.old_client_id = c.client_id
            na.company = c.name
            na.email = c.email
            na.user = u
            na.save()

        for o in LCOperator.objects.all():
            na = Address()
            na.old_operator_id = o.operator_id
            na.company = o.company

            a = LCAddress.objects.get(operator_id=o.operator_id)
            update(a, na, a_ignore)
            na.user = u
            na.save()


        Config.objects.all().delete()
        for c in LCConfig.objects.all():
            nc = Config(name=c.name, value=c.value)
            nc.save()

        LBMJob.objects.all().delete()
        for c in LCJob.objects.all():
            nc = LBMJob()
            nc.old_id = c.job_id
            update(c, nc, j_ignore)

            try:
                lcc = LCClient.objects.get(pk=c.client_id)
                client = Client()
                client.old_id = lcc.client_id
                client.name = lcc.name
                client.save()
            except:
                client = Client()
                client.name = "ERRORED for job " + str(c.job_no)
                client.save()

            nc.client = client

            pub, created = Publication.objects.get_or_create(name=c.publication)
            nc.publication = pub

            

            nc.save()

    LBMJobRoute.objects.all().delete()

    for i in range(1,110):
        for r in LCJobRoute.objects.all()[i*1000:(i+1)*1000]: 
            nr = LBMJobRoute()
            nr.old_id = r.job_route_id
            update(r, nr, jr_ignore)
            
            job = LBMJob.objects.get(old_id=r.job_id)

            nr.job = job

            nr.save()
