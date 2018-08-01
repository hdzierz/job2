from django.db import models
from django.contrib.auth.models import User

import datetime

# Create your models here.


class Config(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    value = models.CharField(max_length=20, blank=True, null=True)


class CfgJobType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="")
    
    def __str__(self):
        return  self.name


class CfgAddressType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="")

    def __str__(self):
        return self.name


class Address(models.Model):
    old_address_id = models.IntegerField(blank=True, null=True, default=None)
    old_operator_id = models.IntegerField(blank=True, null=True, default=None)
    old_client_id = models.IntegerField(blank=True, null=True, default=None)
    old_branch_id = models.IntegerField(blank=True, null=True, default=None)
    typ = models.ManyToManyField(CfgAddressType)

    parent = models.ForeignKey("self", related_name='mother', on_delete=models.PROTECT, blank=True, null=True, default=None)
    sort = models.CharField(max_length=11, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    print_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name2 = models.CharField(max_length=50, blank=True, null=True)
    last_name2 = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    postal_addr = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    postcode = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    phone2 = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    mobile2 = models.CharField(max_length=50, blank=True, null=True)
    mobile3 = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    email2 = models.EmailField(blank=True, null=True)
    email3 = models.EmailField(blank=True, null=True) 
    bank_num = models.CharField(max_length=20, blank=True, null=True)
    gst_num = models.CharField(max_length=20, blank=True, null=True)
    mail_type = models.CharField(max_length=1, blank=True, null=True)
    card_id = models.CharField(max_length=1024, blank=True, null=True)
    alt_mail_type = models.CharField(max_length=1, blank=True, null=True)
    alt_email = models.CharField(max_length=50, blank=True, null=True)
    alt_fax = models.CharField(max_length=50, blank=True, null=True)
    netpass = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.ForeignKey("self", related_name='mother', blank=True, null=True, default=None, on_delete=models.DO_NOTHING)

    def __str__(self):
        ret = self.last_name
        if(self.company):
            ret = self.company
        return str(ret)
    ########### Client additions #########################


class Client(Address):
    invoice_details = models.TextField(blank=True, null=True)
    c_code = models.IntegerField(blank=True, null=True)
    has_discount = models.BooleanField(blank=True, default=False)
    delivery_details = models.TextField(blank=True, null=True)
    net_costs = models.CharField(max_length=20, blank=True, null=True)
    base_price = models.CharField(max_length=20, blank=True, null=True)
    linehaul = models.CharField(max_length=20, blank=True, null=True)
    u_nw_1 = models.TextField(blank=True, null=True)
    u_nw_2 = models.TextField(blank=True, null=True)
    u_nw_3 = models.TextField(blank=True, null=True)
    u_nw_4 = models.TextField(blank=True, null=True)
    u_nw_5 = models.TextField(blank=True, null=True)
    u_nw_6 = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)

class ClientPrice(models.Model):
    client_price_id = models.IntegerField(default=0)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    pa_dist = models.FloatField(blank=True, null=True)
    pa_sdist = models.FloatField(blank=True, null=True)
    pa_cont = models.FloatField(blank=True, null=True)
    pr_u_1 = models.FloatField(blank=True, null=True)
    pr_u_2 = models.FloatField(blank=True, null=True)
    pr_u_3 = models.FloatField(blank=True, null=True)
    pr_u_4 = models.FloatField(blank=True, null=True)
    pr_u_5 = models.FloatField(blank=True, null=True)
    pr_u_6 = models.FloatField(blank=True, null=True)
    from_weight = models.FloatField(blank=True, null=True)
    to_weight = models.FloatField(blank=True, null=True)



class Publication(models.Model):
    name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class CfgAdressSuppType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="")


class AdressSupp(models.Model):
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    typ = models.ForeignKey(CfgAdressSuppType, on_delete=models.PROTECT) 

    street = models.CharField(max_length=255)
    po_box = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    post_code = models.CharField(max_length=255)     


class Island(models.Model):
    name = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=255)
    island = models.ForeignKey(Island, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Area(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    

class Route(models.Model):
    old_id = models.IntegerField(blank=True, null=True, default=None)
    island = models.ForeignKey(Island, on_delete=models.PROTECT)
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    rd = models.CharField(max_length=255,blank=True, null=True)
    post_code =  models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    pmp_areacode = models.IntegerField(blank=True, null=True)
    pmp_runcode = models.IntegerField(blank=True, null=True)
    lifestyle = models.IntegerField(blank=True, null=True)
    farmers = models.IntegerField(blank=True, null=True)
    dairies = models.IntegerField(blank=True, null=True)
    sheep = models.IntegerField(blank=True, null=True)
    beef = models.IntegerField(blank=True, null=True)
    sheepbeef = models.IntegerField(blank=True, null=True)
    dairybeef = models.IntegerField(blank=True, null=True)
    hort = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    seq_region = models.IntegerField(blank=True, null=True)
    seq_area = models.IntegerField(blank=True, null=True)
    seq_code = models.IntegerField(blank=True, null=True)
    is_hidden = models.CharField(max_length=2)
    num_nzfw = models.IntegerField(blank=True, null=True)
    rmt = models.IntegerField(blank=True, null=True)
    rm_rr = models.IntegerField(blank=True, null=True)
    rm_f = models.IntegerField(blank=True, null=True)
    rm_d = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.code


class RouteAff(models.Model):
    route = models.ForeignKey(Route, on_delete=models.PROTECT)
    lbm_dist = models.ForeignKey(Operator, related_name='lbm_dist', on_delete=models.PROTECT)
    lbm_subdist = models.ForeignKey(Operator, related_name='lbm_subdist', on_delete=models.PROTECT)
    lbm_contractor = models.ForeignKey(Operator, related_name='lbm_contractor', on_delete=models.PROTECT)
    lbm_dropoff = models.ForeignKey(Operator, related_name='lbm_dropoff', on_delete=models.PROTECT)

    pcl_dist = models.ForeignKey(Operator, related_name='pcl_dist', on_delete=models.PROTECT)
    pcl_subdist = models.ForeignKey(Operator, related_name='pcl_subdist', on_delete=models.PROTECT)
    pcl_contractor = models.ForeignKey(Operator, related_name='pcl_contractor', on_delete=models.PROTECT)
    pcl_dropoff = models.ForeignKey(Operator, related_name='pcl_dropoff', on_delete=models.PROTECT)

    app_date = models.DateField()

    @staticmethod
    def GetLBMContractor(route, dtt = datetime.datetime.now()):
        res = RouteAff.objects.filter(
            route = route,
            app_date__gt = dtt
        ).order_by('-app_date')

        if res.count() == 0:
            raise Exception("ERROR IN Route Aff: " + str(route) + " not found (" + str(dtt) + ")")
        return res[0]

    @staticmethod
    def GetLBMRoute(op, dtt, tgt):
        if isinstance(tgt, str):
            ras = RouteAff.objects.filter(
                lbm_dist = op,
                typ__name = tgt,
                app_date__gt = dtt,
            ).order_by('-app_date')
        else:
            ras = RouteAff.objects.filter(
                lbm_dist = op,
                typ = tgt,
                app_date__gt = dtt,
            ).order_by('-app_date')

        if ras.count() == 0:
            raise Exception("ERROR IN Route Aff: " + str(op) + " not found (" + dtt + ")")
        return ras[0].route


#from django.db.models.signals import pre_save
#from django.dispatch import receiver
#@receiver(pre_save, sender=Route)
#def my_handler(sender, **kwargs):
