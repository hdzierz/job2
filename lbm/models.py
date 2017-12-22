from django.db import models
from django.contrib.auth.models import User

from master_files.models import *

# Create your models here.



class LBMJob(models.Model):
    old_id = models.IntegerField(blank=True, null=True, default=None)
    purchase_no = models.CharField(max_length=50, blank=True, null=True)
    client = models.ForeignKey(Address, blank=True, null=True, related_name='client')
    publication = models.ForeignKey(Publication, blank=True, null=True)
    job_no = models.IntegerField(blank=True, null=True)
    pmp_job_no = models.CharField(max_length=50, blank=True, null=True)
    lodge_date = models.DateField(blank=True, null=True)
    invoice_no = models.CharField(max_length=50, blank=True, null=True)
    foreign_job_no = models.CharField(max_length=30, blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    contact_notes = models.TextField(default="")
    change_date = models.DateField(blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    inc_linehaul = models.BooleanField(default=False, blank=True)
    dist_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subdist_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    contr_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    freight_charge = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hauler = models.CharField(max_length=30, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    show_comments = models.BooleanField(default=False)
    confirmed = models.CharField(max_length=1, blank=True, null=True)
    finished = models.CharField(max_length=1, blank=True, null=True)
    cancelled = models.CharField(max_length=1, blank=True, null=True)
    lbc_charge = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    dest_type = models.ForeignKey(CfgJobType, blank=True, null=True)
    invoice_qty = models.IntegerField(blank=True, null=True)
    is_regular = models.BooleanField(default=False)
    qty_bbc = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    rate_bbc = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    lbc_charge_bbc = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    is_ioa = models.BooleanField(default=False)
    alt_job_id = models.IntegerField(blank=True, null=True)
    is_att = models.BooleanField(default=False)
    field_surcharge = models.FloatField(blank=True, null=True)
    gst = models.FloatField(blank=True, null=True)
    fuel_surcharge = models.FloatField(blank=True, null=True)
    folding_fee = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)    
    is_deliv_sent = models.BooleanField(default=False)
    is_pay_sent = models.BooleanField(default=False)
    hauler_ni = models.ForeignKey(Address, blank=True, null=True, related_name='hauler_no')
    hauler_si = models.ForeignKey(Address, blank=True, null=True, related_name='hauler_si')
    is_job_details_sent = models.BooleanField(default=False)
    ni_drop_total = models.IntegerField(blank=True, null=True)
    si_drop_total = models.IntegerField(blank=True, null=True)
    desc_bbc = models.CharField(max_length=255, blank=True, null=True)
    add_folding_to_invoice = models.BooleanField(default=False)
    premium = models.FloatField(blank=True, null=True)
    add_premium_to_invoice = models.CharField(max_length=2, blank=True, null=True)
    group = models.IntegerField(blank=True, null=True)
    premium_sell = models.FloatField(blank=True, null=True)
    paper_source = models.CharField(max_length=100, blank=True, null=True)
    has_ni = models.BooleanField(default=False)
    has_si = models.BooleanField(default=False)
    rcd_weight_si = models.IntegerField(blank=True, null=True)
    rcd_weight_ni = models.IntegerField(blank=True, null=True)
    rcd_date_ni = models.DateField(blank=True, null=True)
    rcd_date_si = models.DateField(blank=True, null=True)
    disp_date_si = models.DateField(blank=True, null=True)
    disp_date_ni = models.DateField(blank=True, null=True)
    pick_date_ni = models.DateField(blank=True, null=True)
    pick_date_si = models.DateField(blank=True, null=True)
    initials_ni = models.CharField(max_length=10, blank=True, null=True)
    initials_si = models.CharField(max_length=10, blank=True, null=True)
    rcd_qty_si = models.IntegerField(blank=True, null=True)
    rcd_qty_ni = models.IntegerField(blank=True, null=True)
    bundle_sell = models.FloatField(blank=True, null=True)
    str_group = models.CharField(max_length=255, blank=True, null=True)
    rcd_weight = models.IntegerField(blank=True, null=True)
    rcd_date = models.DateField(blank=True, null=True)
    disp_date = models.DateField(blank=True, null=True)
    pick_date = models.DateField(blank=True, null=True)
    initials = models.CharField(max_length=255, blank=True, null=True)
    rcd_qty = models.IntegerField(blank=True, null=True)
    amount_tot = models.IntegerField(blank=True, null=True)
    l_h_option = models.CharField(max_length=1, default='N')
    manifest_created = models.BooleanField(default=False, blank=True)
    label_printed = models.BooleanField(default=False, blank=True)
    ex_depot_date_si = models.DateField(blank=True, null=True)
    ex_depot_date_ni = models.DateField(blank=True, null=True)
    print_advices = models.BooleanField(default=False, blank=True)
    l_h_option = models.CharField(max_length=1, blank=True, null=True)
    label_printed = models.IntegerField(blank=True, null=True)
    manifest_created = models.IntegerField(blank=True, null=True)
    linehaul_a = models.CharField(max_length=255, blank=True, null=True)
    ex_depot_date_si = models.DateField(blank=True, null=True)
    ex_depot_date_ni = models.DateField(blank=True, null=True)
    ex_depot_date = models.DateField(blank=True, null=True)
    qty_per_bundle_ni = models.IntegerField(blank=True, null=True)
    qty_per_bundle_si = models.IntegerField(blank=True, null=True)

    def __str__(self):
        if(self.job_no):
            return str(self.job_no)
        else:
            return "unkown"



class LBMJobRoute(models.Model):
    old_id = models.IntegerField(blank=True, null=True, default=None)
    old_dist_id = models.IntegerField(blank=True, null=True, default=None)
    old_subdist_id = models.IntegerField(blank=True, null=True, default=None)
    old_contractor_id = models.IntegerField(blank=True, null=True, default=None)
    old_dropoff_id = models.IntegerField(blank=True, null=True, default=None)
    old_alt_ropoff_id = models.IntegerField(blank=True, null=True, default=None)
    old_doff_id = models.IntegerField(blank=True, null=True, default=None)
    job = models.ForeignKey(LBMJob, blank=True, null=True)
    route = models.ForeignKey(Route, blank=True, null=True)
    dist = models.ForeignKey(Address, blank=True, null=True, related_name='dist')
    subdist = models.ForeignKey(Address, blank=True, null=True, related_name='subdist')
    contractor = models.ForeignKey(Address, blank=True, null=True, related_name='contractor')
    dropoff = models.ForeignKey(Address, blank=True, null=True, related_name='dropoff')
    dest_type = models.ForeignKey(CfgJobType, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    external = models.CharField(max_length=5, blank=True, null=True)
    is_edited = models.BooleanField(default=False)
    version = models.CharField(max_length=30, blank=True, null=True)
    bundle_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    orig_amt = models.IntegerField(blank=True, null=True)
    alt_dropoff_id = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    subdist_rate_red = models.FloatField(default=1)

