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
        fnlc = f.name
        if(fnlc not in ignore):
            try:
                val = getattr(c, fnlc)
            except:
                pass
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

c_master = True 
c_lbm = True

def run():
    if c_master:
        Route.objects.all().delete()
        for c in LCRoute.objects.all():
            print("Route: " + c.code)
            nc = Route()
            update(c, nc, ignore)
            island, created = Island.objects.get_or_create(name=c.island)
            nc.island = island
            region, created = Region.objects.get_or_create(name=c.region, island=island)
            nc.region=region
            area, created = Area.objects.get_or_create(name=c.area, region=region)
            nc.area = area
            nc.rd = c.code
            nc.old_id = c.route_id
            nc.save()

        Address.objects.all().delete()
        for a in LCAddress.objects.all():
            print("OP: " + a.name)
            op = LCOperator.objects.get(pk=a.operator_id)    

            na = Address()
            na.old_id = a.address_id
            na.old_operator_id = a.operator_id
            na.old_client_id = a.client_id
            update(a, na, a_ignore)
            update(op, na, a_ignore)
            na.last_name = a.name
            na.last_name2 = a.name2
            na.save()

            if(op.is_dist == 'Y'):
                na.typ.add(CfgAddressType.objects.get(name="lbm_dist"))
                na.typ.add(CfgAddressType.objects.get(name="pcl_dist"))
            if(op.is_subdist == 'Y'):
                na.typ.add(CfgAddressType.objects.get(name="lbm_subdist"))
                na.typ.add(CfgAddressType.objects.get(name="pcl_subdist"))
            if(op.is_contr == 'Y'):
                na.typ.add(CfgAddressType.objects.get(name="lbm_contractor"))
                na.typ.add(CfgAddressType.objects.get(name="pcl_contractor"))
            if(op.is_dropoff == 'Y'):
                na.typ.add(CfgAddressType.objects.get(name="lbm_dropoff"))
                na.typ.add(CfgAddressType.objects.get(name="pcl_dropoff"))
            if(op.is_alt_dropoff == 'Y'):
                na.typ.add(CfgAddressType.objects.get(name="lbm_alt_dropoff"))

        
        for client in LCClient.objects.all():
            print("Client: " + client.name)
            na = Address()
            na.old_client_id = client.client_id
            na.company = client.name
            
            update(client, na, a_ignore) 
            na.save()

            if client.is_hauler == 'Y':
                na.typ.add(CfgAddressType.objects.get(name="lbm_hauler"))
            else:
                na.typ.add(CfgAddressType.objects.get(name="lbm_client"))


        Config.objects.all().delete()
        for c in LCConfig.objects.all():
            nc = Config(name=c.name, value=c.value)
            nc.save()

    if c_lbm:
        LBMJob.objects.all().delete()
        for c in LCJob.objects.all():
            print("Job: " + str(c.job_no))
            nc = LBMJob()
            nc.old_id = c.job_id
            update(c, nc, j_ignore)

            try:
                client = Address.objects.get(old_client_id=c.client_id)
            except:
                client = Address()
                client.name = "ERRORED for job " + str(c.job_no)
                client.save()

            nc.client = client

            pub, created = Publication.objects.get_or_create(name=c.publication, client=client)
            nc.publication = pub

            nc.dest_type = CfgJobType.objects.get(name=c.dest_type)

            nc.save()

        LBMJobRoute.objects.all().delete()

        for i in range(1,110):
            print("JR: " + str(i))
            for r in LCJobRoute.objects.all()[i*1000:(i+1)*1000]:
                nr = LBMJobRoute()
                nr.old_id = r.job_route_id
                update(r, nr, jr_ignore)
                
                job = LBMJob.objects.get(old_id=r.job_id)
                route = Route.objects.get(old_id=r.route_id)
                try:
                    dist = Address.objects.get(old_operator_id=r.dist_id)
                    subdist = Address.objects.get(old_operator_id=r.subdist_id)
                    contractor = Address.objects.get(old_operator_id=r.contractor_id)
                    dropoff = Address.objects.get(old_operator_id=r.dropoff_id)
                    #alt_dropoff = Address.objects.get(old_operator_id=r.alt_dropoff_id)
                except:
                    dist = None
                    subdist = None
                    contractor = None
                    dropoff = None

                nr.job = job
                nr.route = route
                nr.dist = dist
                nr.subdist = subdist
                nr.contractor = contractor
                nr.dropoff = dropoff   
                nc.dest_type = CfgJobType.objects.get(name=r.dest_type)
 
                nr.save()
