import django_tables2 as tables
from lbm.models import *


class RouteTable(tables.Table):

    class Meta:
        template="data_table.html"
        model = Route
        fields = ("island", "area", "region", "code","description" )
