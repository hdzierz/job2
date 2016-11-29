from lbm.models import *
from coural_legacy.models import *

ignore = ["island", "area", "region"]


def run():
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
