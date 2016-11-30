from lbm.models import *
from coural_legacy.models import *

ignore = ["island", "area", "region"]
a_ignore = ["user"]

def run():
    Route.objects.all().delete()
    for c in LCRoute.objects.all():
        nc = Route()
        for f in c._meta.get_fields():
            print(f.name)
            fnlc = f.name
            if(fnlc not in ignore):
                setattr(nc, f.name, getattr(c, fnlc))
        island, created = Island.objects.get_or_create(name=c.island)
        nc.island = island
        area, created = Area.objects.get_or_create(name=c.area)
        nc.area = area
        region, created = Region.objects.get_or_create(name=c.region)
        nc.region=region
        nc.rd = c.code
        nc.save()

    ct = 0
    Address.objects.all().delete()
    for a in LCAddress.objects.all():
        na = Address()
        for f in a._meta.get_fields():
            print(f.name)
            if(f.name not in a_ignore):
                setattr(na, f.name, getattr(a, f.name))
        
        user, created = User.objects.get_or_create(
            username=a.name,
            password = 'adjfq378r6',
        )
    
        ct += 1
        if(not created):
            user = User(
                username=a.name + '_' + str(ct),
                password = 'adjfq378r6',
            )
            user.save()
        na.user = user
        na.save() 
        
