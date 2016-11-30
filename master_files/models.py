from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Address(models.Model):
    #operator = models.ForeignKey(Operator, blank=True, null=True)
    user = models.OneToOneField(User)
    sort = models.CharField(max_length=11, blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    salutation = models.CharField(max_length=30, blank=True, null=True)
    salutation2 = models.CharField(max_length=20, blank=True, null=True)
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
    fax = models.CharField(max_length=50, blank=True, null=True)
    bank_num = models.CharField(max_length=20, blank=True, null=True)
    gst_num = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=11, blank=True, null=True)
    mail_type = models.CharField(max_length=1, blank=True, null=True)
    card_id = models.CharField(max_length=20, blank=True, null=True)
    alt_mail_type = models.CharField(max_length=1, blank=True, null=True)
    alt_email = models.CharField(max_length=50, blank=True, null=True)
    alt_fax = models.CharField(max_length=50, blank=True, null=True)
    netpass = models.CharField(max_length=255, blank=True, null=True)


class Operator(models.Model):
    address = models.ForeignKey(Address, blank=True, null=True)
    is_dist = models.CharField(max_length=1, blank=True, null=True)
    is_subdist = models.CharField(max_length=1, blank=True, null=True)
    is_dropoff = models.CharField(max_length=1, blank=True, null=True)
    is_contr = models.CharField(max_length=1, blank=True, null=True)
    circ_drop = models.IntegerField(blank=True, null=True)
    shares = models.IntegerField(blank=True, null=True)
    alias = models.TextField(blank=True, null=True)
    contract = models.CharField(max_length=1, blank=True, null=True)
    agency = models.CharField(max_length=1, blank=True, null=True)
    date_started = models.DateField(blank=True, null=True)
    date_left = models.DateField(blank=True, null=True)
    deliv_notes = models.TextField(blank=True, null=True)
    env_deliv_notes = models.TextField(blank=True, null=True)
    do_address = models.CharField(max_length=100, blank=True, null=True)
    do_city = models.CharField(max_length=50, blank=True, null=True)
    latest_dep = models.TextField(blank=True, null=True)
    is_current = models.CharField(max_length=1)
    is_shareholder = models.CharField(max_length=1, blank=True, null=True)
    share_bought = models.DateField(blank=True, null=True)
    share_sold = models.DateField(blank=True, null=True)
    share_notes = models.TextField(blank=True, null=True)
    is_alt_dropoff = models.CharField(max_length=1, blank=True, null=True)
    subdist_seq = models.IntegerField(blank=True, null=True)
    is_hauler_ni = models.IntegerField(blank=True, null=True)
    is_hauler_si = models.IntegerField(blank=True, null=True)
    rate_red_fact = models.FloatField()
    parcel_send_di = models.CharField(max_length=2, blank=True, null=True)
    send_contr_sheet = models.CharField(max_length=2, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    linehaul_a = models.CharField(max_length=255, blank=True, null=True)
    linehaul_a_type = models.CharField(max_length=255, blank=True, null=True)
    linehaul_a_bin = models.CharField(max_length=255, blank=True, null=True)
    linehaul_b_bin = models.CharField(max_length=255, blank=True, null=True)
    linehaul_b_type = models.CharField(max_length=255, blank=True, null=True)
    linehaul_b = models.CharField(max_length=255, blank=True, null=True)
    ph_desk = models.TextField(blank=True, null=True)
    rate_code = models.CharField(max_length=255, blank=True, null=True)
    depot_rent = models.FloatField(blank=True, null=True)
    scanner_no1 = models.CharField(max_length=255, blank=True, null=True)
    scanner_no2 = models.CharField(max_length=255, blank=True, null=True)
    scanner_no3 = models.CharField(max_length=255, blank=True, null=True)
    scanner_no4 = models.CharField(max_length=255, blank=True, null=True)
    scanner_phone_no1 = models.CharField(max_length=255, blank=True, null=True)
    scanner_phone_no2 = models.CharField(max_length=255, blank=True, null=True)
    scanner_phone_no3 = models.CharField(max_length=255, blank=True, null=True)
    scanner_phone_no4 = models.CharField(max_length=255, blank=True, null=True)
    scanner_email = models.CharField(max_length=255, blank=True, null=True)
    scanner_charge = models.FloatField(blank=True, null=True)
    mobile_pay = models.FloatField(blank=True, null=True)


class Client(models.Model):
    address = models.ForeignKey(Address, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    card_id = models.CharField(max_length=30, blank=True, null=True)
    contact_details = models.TextField(blank=True, null=True)
    is_parcel_courier = models.IntegerField(blank=True, null=True)
    invoice_details = models.TextField(blank=True, null=True)
    c_code = models.IntegerField(blank=True, null=True)
    has_discount = models.IntegerField(blank=True, null=True)
    delivery_details = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    is_hauler = models.IntegerField(blank=True, null=True)
    net_costs = models.CharField(max_length=20, blank=True, null=True)
    base_price = models.CharField(max_length=20, blank=True, null=True)
    linehaul = models.CharField(max_length=20, blank=True, null=True)
    is_linehaul = models.IntegerField()
    u_nw_1 = models.TextField(blank=True, null=True)
    u_nw_2 = models.TextField(blank=True, null=True)
    u_nw_3 = models.TextField(blank=True, null=True)
    u_nw_4 = models.TextField(blank=True, null=True)
    u_nw_5 = models.TextField(blank=True, null=True)
    u_nw_6 = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    is_operator = models.IntegerField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)


class Publication(models.Model):
    name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, blank=True, null=True)


class Island(models.Model):
    name = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Area(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class RD(models.Model):
    name = models.CharField(max_length=255)


class Route(models.Model):
    island = models.ForeignKey(Island)
    area = models.ForeignKey(Area)
    region = models.ForeignKey(Region)
    code = models.CharField(max_length=255,blank=True, null=True) 
    description = models.TextField(blank=True, null=True)
    pmp_areacode = models.IntegerField(blank=True, null=True)
    pmp_runcode = models.IntegerField(blank=True, null=True)
    num_lifestyle = models.IntegerField(blank=True, null=True)
    num_farmers = models.IntegerField(blank=True, null=True)
    num_dairies = models.IntegerField(blank=True, null=True)
    num_sheep = models.IntegerField(blank=True, null=True)
    num_beef = models.IntegerField(blank=True, null=True)
    num_sheepbeef = models.IntegerField(blank=True, null=True)
    num_dairybeef = models.IntegerField(blank=True, null=True)
    num_hort = models.IntegerField(blank=True, null=True)
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


