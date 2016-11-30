# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    operator_id = models.IntegerField(blank=True, null=True)
    sort = models.CharField(max_length=11, blank=True, null=True)
    salutation = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    salutation2 = models.CharField(max_length=20, blank=True, null=True)
    first_name2 = models.CharField(max_length=50, blank=True, null=True)
    name2 = models.CharField(max_length=50, blank=True, null=True)
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
    email = models.CharField(max_length=50, blank=True, null=True)
    etext = models.CharField(max_length=30, blank=True, null=True)
    bank_num = models.CharField(max_length=20, blank=True, null=True)
    gst_num = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=11, blank=True, null=True)
    mail_type = models.CharField(max_length=1, blank=True, null=True)
    card_id = models.CharField(max_length=20, blank=True, null=True)
    alt_mail_type = models.CharField(max_length=1, blank=True, null=True)
    alt_email = models.CharField(max_length=50, blank=True, null=True)
    alt_fax = models.CharField(max_length=50, blank=True, null=True)
    client_id = models.IntegerField(blank=True, null=True)
    netpass = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address'


class AddressCopy(models.Model):
    address_id = models.AutoField(primary_key=True)
    operator_id = models.IntegerField(blank=True, null=True)
    sort = models.CharField(max_length=11, blank=True, null=True)
    salutation = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    salutation2 = models.CharField(max_length=20, blank=True, null=True)
    first_name2 = models.CharField(max_length=50, blank=True, null=True)
    name2 = models.CharField(max_length=50, blank=True, null=True)
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
    email = models.CharField(max_length=50, blank=True, null=True)
    etext = models.CharField(max_length=30, blank=True, null=True)
    bank_num = models.CharField(max_length=20, blank=True, null=True)
    gst_num = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=11, blank=True, null=True)
    mail_type = models.CharField(max_length=1, blank=True, null=True)
    card_id = models.CharField(max_length=20, blank=True, null=True)
    alt_mail_type = models.CharField(max_length=1, blank=True, null=True)
    alt_email = models.CharField(max_length=50, blank=True, null=True)
    alt_fax = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address_copy'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthPermission(models.Model):
    name = models.CharField(max_length=50)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Branch(models.Model):
    branch_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'branch'


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
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

    class Meta:
        managed = False
        db_table = 'client'


class ClientBranch(models.Model):
    client_branch_id = models.AutoField(primary_key=True)
    client_id = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_branch'


class ClientPrice(models.Model):
    client_price_id = models.AutoField(primary_key=True)
    client_id = models.IntegerField(blank=True, null=True)
    weight = models.CharField(max_length=20, blank=True, null=True)
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

    class Meta:
        managed = False
        db_table = 'client_price'


class ClientPub(models.Model):
    client_pub_id = models.AutoField(primary_key=True)
    client_id = models.IntegerField()
    client_pub_num = models.IntegerField(blank=True, null=True)
    pub_weekly = models.TextField(blank=True, null=True)
    pub_fortnightly = models.TextField(blank=True, null=True)
    pub_monthly = models.TextField(blank=True, null=True)
    pub_other = models.TextField(blank=True, null=True)
    pub_weekly_ff = models.IntegerField(blank=True, null=True)
    pub_fortnightly_ff = models.IntegerField(blank=True, null=True)
    pub_monthly_ff = models.IntegerField(blank=True, null=True)
    pub_other_ff = models.IntegerField(blank=True, null=True)
    pub_weekly_lh = models.IntegerField(blank=True, null=True)
    pub_fortnightly_lh = models.IntegerField(blank=True, null=True)
    pub_monthly_lh = models.IntegerField(blank=True, null=True)
    pub_other_lh = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_pub'


class ClientPubs(models.Model):
    client_pub_id = models.AutoField(primary_key=True)
    client_id = models.IntegerField()
    publication = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_pubs'


class Config(models.Model):
    config_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    value = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'config'


class ControlHistory(models.Model):
    control_history_id = models.AutoField(primary_key=True)
    page = models.TextField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'control_history'


class ControlLogin(models.Model):
    control_login_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    passwd = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'control_login'


class CurrentJobScreen(models.Model):
    current_job_screen_id = models.AutoField(primary_key=True)
    publication = models.TextField(blank=True, null=True)
    client_id = models.IntegerField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'current_job_screen'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    user_id = models.IntegerField()
    content_type_id = models.IntegerField(blank=True, null=True)
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EmailLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    time_point = models.DateTimeField()
    error_count = models.IntegerField(blank=True, null=True)
    error_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_log'


class Howard(models.Model):
    job_id = models.IntegerField(blank=True, null=True)
    ticket_no = models.IntegerField(blank=True, null=True)
    is_redeemed_d = models.IntegerField(db_column='is_redeemed_D', blank=True, null=True)  # Field name made lowercase.
    order_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'howard'


class ImportC(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    cust_code = models.CharField(db_column='Cust_Code', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    post_code = models.CharField(db_column='Post_Code', max_length=255, blank=True, null=True)  # Field name made lowercase.
    del_name = models.CharField(db_column='Del_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    del_add1 = models.CharField(db_column='Del_Add1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    del_add2 = models.CharField(db_column='Del_Add2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    del_add3 = models.CharField(db_column='Del_Add3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    card_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'import_c'


class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    job_id = models.IntegerField(blank=True, null=True)
    purchase_no = models.CharField(max_length=50, blank=True, null=True)
    client_id = models.IntegerField(blank=True, null=True)
    client_pub_id = models.IntegerField(blank=True, null=True)
    invoice_no = models.CharField(max_length=50, blank=True, null=True)
    foreign_job_no = models.CharField(max_length=30, blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    change_date = models.DateField(blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    dist_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subdist_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    contr_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    malcove_charge = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    malcove_invoice_no = models.CharField(max_length=20, blank=True, null=True)
    coural_allowance = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    freight = models.CharField(max_length=30, blank=True, null=True)
    job_no = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice'


class InvoiceArchive(models.Model):
    invoice_id = models.IntegerField()
    job_id = models.IntegerField(blank=True, null=True)
    purchase_no = models.CharField(max_length=50, blank=True, null=True)
    client_id = models.IntegerField(blank=True, null=True)
    client_pub_id = models.IntegerField(blank=True, null=True)
    invoice_no = models.CharField(max_length=50, blank=True, null=True)
    foreign_job_no = models.CharField(max_length=30, blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    change_date = models.DateField(blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    dist_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subdist_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    contr_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    malcove_charge = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    malcove_invoice_no = models.CharField(max_length=20, blank=True, null=True)
    coural_allowance = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    freight = models.CharField(max_length=30, blank=True, null=True)
    job_no = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_archive'


class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    purchase_no = models.CharField(max_length=50, blank=True, null=True)
    client_id = models.IntegerField(blank=True, null=True)
    publication = models.CharField(max_length=200, blank=True, null=True)
    client_pub_id = models.IntegerField(blank=True, null=True)
    job_no = models.IntegerField(blank=True, null=True)
    pmp_job_no = models.CharField(max_length=50, blank=True, null=True)
    lodge_date = models.DateField(blank=True, null=True)
    job_no_add = models.CharField(max_length=7, blank=True, null=True)
    invoice_no = models.CharField(max_length=50, blank=True, null=True)
    foreign_job_no = models.CharField(max_length=30, blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    change_date = models.DateField(blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    inc_linehaul = models.CharField(max_length=1)
    dist_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subdist_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    contr_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    freight_charge = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hauler = models.CharField(max_length=30, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    show_comments = models.CharField(max_length=255, blank=True, null=True)
    confirmed = models.CharField(max_length=1, blank=True, null=True)
    finished = models.CharField(max_length=1, blank=True, null=True)
    cancelled = models.CharField(max_length=1, blank=True, null=True)
    lbc_charge = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    dest_type = models.CharField(max_length=30, blank=True, null=True)
    invoice_qty = models.IntegerField(blank=True, null=True)
    is_regular = models.CharField(max_length=1, blank=True, null=True)
    qty_bbc = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    rate_bbc = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    lbc_charge_bbc = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    is_ioa = models.CharField(max_length=1, blank=True, null=True)
    alt_job_id = models.IntegerField(blank=True, null=True)
    is_quote = models.CharField(max_length=1, blank=True, null=True)
    is_att = models.CharField(max_length=1, blank=True, null=True)
    field_surcharge = models.FloatField(blank=True, null=True)
    gst = models.FloatField(blank=True, null=True)
    fuel_surcharge = models.FloatField(blank=True, null=True)
    folding_fee = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    is_deliv_sent = models.IntegerField(blank=True, null=True)
    is_pay_sent = models.IntegerField(blank=True, null=True)
    hauler_ni_id = models.IntegerField(blank=True, null=True)
    hauler_si_id = models.IntegerField(blank=True, null=True)
    is_job_details_sent = models.IntegerField(blank=True, null=True)
    ni_drop_total = models.IntegerField(blank=True, null=True)
    si_drop_total = models.IntegerField(blank=True, null=True)
    desc_bbc = models.CharField(max_length=255, blank=True, null=True)
    add_folding_to_invoice = models.CharField(max_length=2, blank=True, null=True)
    premium = models.FloatField(blank=True, null=True)
    add_premium_to_invoice = models.CharField(max_length=2, blank=True, null=True)
    group = models.IntegerField(blank=True, null=True)
    premium_sell = models.FloatField(blank=True, null=True)
    paper_source = models.CharField(max_length=100, blank=True, null=True)
    has_ni = models.IntegerField(blank=True, null=True)
    has_si = models.IntegerField(blank=True, null=True)
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
    print_advices = models.CharField(max_length=2, blank=True, null=True)
    l_h_option = models.CharField(max_length=1, blank=True, null=True)
    label_printed = models.IntegerField(blank=True, null=True)
    manifest_created = models.IntegerField(blank=True, null=True)
    linehaul_a = models.CharField(max_length=255, blank=True, null=True)
    ex_depot_date_si = models.DateField(blank=True, null=True)
    ex_depot_date_ni = models.DateField(blank=True, null=True)
    ex_depot_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job'


class JobArchive(models.Model):
    job_id = models.IntegerField(primary_key=True)
    purchase_no = models.CharField(max_length=50, blank=True, null=True)
    client_id = models.IntegerField(blank=True, null=True)
    publication = models.CharField(max_length=200, blank=True, null=True)
    client_pub_id = models.IntegerField(blank=True, null=True)
    job_no = models.IntegerField(blank=True, null=True)
    pmp_job_no = models.CharField(max_length=50, blank=True, null=True)
    lodge_date = models.DateField(blank=True, null=True)
    job_no_add = models.CharField(max_length=7, blank=True, null=True)
    invoice_no = models.CharField(max_length=50, blank=True, null=True)
    foreign_job_no = models.CharField(max_length=30, blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    change_date = models.DateField(blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    inc_linehaul = models.CharField(max_length=1)
    dist_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subdist_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    contr_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    freight_charge = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hauler = models.CharField(max_length=30, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    show_comments = models.CharField(max_length=255, blank=True, null=True)
    confirmed = models.CharField(max_length=1, blank=True, null=True)
    finished = models.CharField(max_length=1, blank=True, null=True)
    cancelled = models.CharField(max_length=1, blank=True, null=True)
    lbc_charge = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    dest_type = models.CharField(max_length=30, blank=True, null=True)
    invoice_qty = models.IntegerField(blank=True, null=True)
    is_regular = models.CharField(max_length=1, blank=True, null=True)
    qty_bbc = models.IntegerField(blank=True, null=True)
    rate_bbc = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    lbc_charge_bbc = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    is_ioa = models.CharField(max_length=1, blank=True, null=True)
    alt_job_id = models.IntegerField(blank=True, null=True)
    is_quote = models.CharField(max_length=1, blank=True, null=True)
    is_att = models.CharField(max_length=1, blank=True, null=True)
    field_surcharge = models.FloatField(blank=True, null=True)
    gst = models.FloatField(blank=True, null=True)
    fuel_surcharge = models.FloatField(blank=True, null=True)
    folding_fee = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    is_deliv_sent = models.IntegerField(blank=True, null=True)
    is_pay_sent = models.IntegerField(blank=True, null=True)
    hauler_ni_id = models.IntegerField(blank=True, null=True)
    hauler_si_id = models.IntegerField(blank=True, null=True)
    is_job_details_sent = models.IntegerField(blank=True, null=True)
    ni_drop_total = models.FloatField(blank=True, null=True)
    si_drop_total = models.FloatField(blank=True, null=True)
    desc_bbc = models.CharField(max_length=255, blank=True, null=True)
    add_folding_to_invoice = models.CharField(max_length=2, blank=True, null=True)
    premium = models.FloatField(blank=True, null=True)
    add_premium_to_invoice = models.CharField(max_length=2, blank=True, null=True)
    group = models.IntegerField(blank=True, null=True)
    premium_sell = models.FloatField(blank=True, null=True)
    paper_source = models.CharField(max_length=100, blank=True, null=True)
    rcd_weight_si = models.IntegerField(blank=True, null=True)
    rcd_weight_ni = models.IntegerField(blank=True, null=True)
    rcd_date_ni = models.DateField(blank=True, null=True)
    rcd_date_si = models.DateField(blank=True, null=True)
    disp_date_si = models.DateField(blank=True, null=True)
    disp_date_ni = models.DateField(blank=True, null=True)
    pick_date_ni = models.DateField(blank=True, null=True)
    pick_date_si = models.DateField(blank=True, null=True)
    initials_ni = models.DateField(blank=True, null=True)
    initials_si = models.DateField(blank=True, null=True)
    rcd_qty_si = models.IntegerField(blank=True, null=True)
    rcd_qty_ni = models.IntegerField(blank=True, null=True)
    bundle_sell = models.FloatField(blank=True, null=True)
    str_group = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_archive'


class JobCopy(models.Model):
    job_id = models.AutoField(primary_key=True)
    purchase_no = models.CharField(max_length=50, blank=True, null=True)
    client_id = models.IntegerField(blank=True, null=True)
    client_pub_id = models.IntegerField(blank=True, null=True)
    job_no = models.CharField(max_length=11, blank=True, null=True)
    invoice_no = models.CharField(max_length=50, blank=True, null=True)
    foreign_job_no = models.CharField(max_length=30, blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    change_date = models.DateField(blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    dist_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subdist_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    contr_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    freight_charge = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hauler = models.CharField(max_length=30, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    confirmed = models.CharField(max_length=1, blank=True, null=True)
    finished = models.CharField(max_length=1, blank=True, null=True)
    cancelled = models.CharField(max_length=1, blank=True, null=True)
    lbc_charge = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    dest_type = models.CharField(max_length=30, blank=True, null=True)
    invoice_qty = models.IntegerField(blank=True, null=True)
    is_regular = models.CharField(max_length=1, blank=True, null=True)
    qty_bbc = models.IntegerField(blank=True, null=True)
    rate_bbc = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    lbc_charge_bbc = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_copy'


class JobHoward(models.Model):
    job_id = models.IntegerField()
    purchase_no = models.CharField(max_length=50, blank=True, null=True)
    client_id = models.IntegerField(blank=True, null=True)
    publication = models.CharField(max_length=200, blank=True, null=True)
    client_pub_id = models.IntegerField(blank=True, null=True)
    job_no = models.IntegerField(blank=True, null=True)
    pmp_job_no = models.CharField(max_length=50, blank=True, null=True)
    lodge_date = models.DateField(blank=True, null=True)
    job_no_add = models.CharField(max_length=7, blank=True, null=True)
    invoice_no = models.CharField(max_length=50, blank=True, null=True)
    foreign_job_no = models.CharField(max_length=30, blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    change_date = models.DateField(blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    inc_linehaul = models.CharField(max_length=1)
    dist_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subdist_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    contr_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    freight_charge = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hauler = models.CharField(max_length=30, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    show_comments = models.CharField(max_length=255, blank=True, null=True)
    confirmed = models.CharField(max_length=1, blank=True, null=True)
    finished = models.CharField(max_length=1, blank=True, null=True)
    cancelled = models.CharField(max_length=1, blank=True, null=True)
    lbc_charge = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    dest_type = models.CharField(max_length=30, blank=True, null=True)
    invoice_qty = models.IntegerField(blank=True, null=True)
    is_regular = models.CharField(max_length=1, blank=True, null=True)
    qty_bbc = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    rate_bbc = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    lbc_charge_bbc = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    is_ioa = models.CharField(max_length=1, blank=True, null=True)
    alt_job_id = models.IntegerField(blank=True, null=True)
    is_quote = models.CharField(max_length=1, blank=True, null=True)
    is_att = models.CharField(max_length=1, blank=True, null=True)
    field_surcharge = models.FloatField(blank=True, null=True)
    gst = models.FloatField(blank=True, null=True)
    fuel_surcharge = models.FloatField(blank=True, null=True)
    folding_fee = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    is_deliv_sent = models.IntegerField(blank=True, null=True)
    is_pay_sent = models.IntegerField(blank=True, null=True)
    hauler_ni_id = models.IntegerField(blank=True, null=True)
    hauler_si_id = models.IntegerField(blank=True, null=True)
    is_job_details_sent = models.IntegerField(blank=True, null=True)
    ni_drop_total = models.FloatField(blank=True, null=True)
    si_drop_total = models.FloatField(blank=True, null=True)
    desc_bbc = models.CharField(max_length=255, blank=True, null=True)
    add_folding_to_invoice = models.CharField(max_length=2, blank=True, null=True)
    premium = models.FloatField(blank=True, null=True)
    add_premium_to_invoice = models.CharField(max_length=2, blank=True, null=True)
    group = models.IntegerField(blank=True, null=True)
    premium_sell = models.FloatField(blank=True, null=True)
    paper_source = models.CharField(max_length=100, blank=True, null=True)
    rcd_qty = models.FloatField(blank=True, null=True)
    rcd_weight = models.FloatField(blank=True, null=True)
    disp_date = models.DateField(blank=True, null=True)
    pick_date = models.DateField(blank=True, null=True)
    rcd_date = models.DateField(blank=True, null=True)
    initials = models.CharField(max_length=255, blank=True, null=True)
    has_ni = models.IntegerField(blank=True, null=True)
    has_si = models.IntegerField(blank=True, null=True)
    amount_tot = models.IntegerField(blank=True, null=True)
    rcd_weight_si = models.FloatField(blank=True, null=True)
    rcd_weight_ni = models.FloatField(blank=True, null=True)
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

    class Meta:
        managed = False
        db_table = 'job_howard'


class JobRoute(models.Model):
    job_route_id = models.AutoField(primary_key=True)
    job_id = models.IntegerField(blank=True, null=True)
    route_id = models.IntegerField(blank=True, null=True)
    concoll = models.CharField(max_length=1, blank=True, null=True)
    dest_type = models.CharField(max_length=20, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    external = models.CharField(max_length=5, blank=True, null=True)
    is_edited = models.CharField(max_length=1, blank=True, null=True)
    version = models.CharField(max_length=30, blank=True, null=True)
    bundle_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    orig_amt = models.IntegerField(blank=True, null=True)
    alt_dropoff_id = models.IntegerField(blank=True, null=True)
    dropoff_id = models.IntegerField(blank=True, null=True)
    doff = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    dist_id = models.IntegerField(blank=True, null=True)
    subdist_id = models.IntegerField(blank=True, null=True)
    contractor_id = models.IntegerField(blank=True, null=True)
    subdist_rate_red = models.FloatField()
    subdist_rate_red_bu = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_route'


class JobRouteArchive(models.Model):
    job_route_id = models.IntegerField(primary_key=True)
    job_id = models.IntegerField(blank=True, null=True)
    route_id = models.IntegerField(blank=True, null=True)
    concoll = models.CharField(max_length=1, blank=True, null=True)
    dest_type = models.CharField(max_length=20, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    external = models.CharField(max_length=5, blank=True, null=True)
    is_edited = models.CharField(max_length=1, blank=True, null=True)
    version = models.CharField(max_length=30, blank=True, null=True)
    bundle_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    orig_amt = models.IntegerField(blank=True, null=True)
    alt_dropoff_id = models.IntegerField(blank=True, null=True)
    dropoff_id = models.IntegerField(blank=True, null=True)
    doff = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    dist_id = models.IntegerField(blank=True, null=True)
    subdist_id = models.IntegerField(blank=True, null=True)
    contractor_id = models.IntegerField(blank=True, null=True)
    subdist_rate_red = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_route_archive'


class JobRouteNew(models.Model):
    job_route_id = models.AutoField(primary_key=True)
    job_id = models.IntegerField(blank=True, null=True)
    route_id = models.IntegerField(blank=True, null=True)
    concoll = models.CharField(max_length=1, blank=True, null=True)
    dest_type = models.CharField(max_length=20, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    external = models.CharField(max_length=5, blank=True, null=True)
    is_edited = models.CharField(max_length=1, blank=True, null=True)
    version = models.CharField(max_length=30, blank=True, null=True)
    bundle_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    orig_amt = models.IntegerField(blank=True, null=True)
    alt_dropoff_id = models.IntegerField(blank=True, null=True)
    dropoff_id = models.IntegerField(blank=True, null=True)
    doff = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    dist_id = models.IntegerField(blank=True, null=True)
    subdist_id = models.IntegerField(blank=True, null=True)
    contractor_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_route_new'


class JobRouteTemp(models.Model):
    job_route_id = models.AutoField(primary_key=True)
    job_id = models.IntegerField(blank=True, null=True)
    route_id = models.IntegerField(blank=True, null=True)
    concoll = models.CharField(max_length=1, blank=True, null=True)
    dest_type = models.CharField(max_length=20, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    external = models.CharField(max_length=5, blank=True, null=True)
    is_edited = models.CharField(max_length=1, blank=True, null=True)
    version = models.CharField(max_length=30, blank=True, null=True)
    bundle_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    orig_amt = models.IntegerField(blank=True, null=True)
    alt_dropoff_id = models.IntegerField(blank=True, null=True)
    doff = models.IntegerField(blank=True, null=True)
    dist_id = models.IntegerField(blank=True, null=True)
    subdist_id = models.IntegerField(blank=True, null=True)
    contractor_id = models.IntegerField(blank=True, null=True)
    dropoff_id = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_route_temp'


class JobTemp(models.Model):
    job_id = models.AutoField(primary_key=True)
    purchase_no = models.CharField(max_length=50, blank=True, null=True)
    client_id = models.IntegerField(blank=True, null=True)
    publication = models.CharField(max_length=200, blank=True, null=True)
    client_pub_id = models.IntegerField(blank=True, null=True)
    job_no = models.CharField(max_length=11, blank=True, null=True)
    invoice_no = models.CharField(max_length=50, blank=True, null=True)
    foreign_job_no = models.CharField(max_length=30, blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    change_date = models.DateField(blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    dist_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subdist_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    contr_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    freight_charge = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hauler = models.CharField(max_length=30, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    confirmed = models.CharField(max_length=1, blank=True, null=True)
    finished = models.CharField(max_length=1, blank=True, null=True)
    cancelled = models.CharField(max_length=1, blank=True, null=True)
    lbc_charge = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    dest_type = models.CharField(max_length=30, blank=True, null=True)
    invoice_qty = models.IntegerField(blank=True, null=True)
    is_regular = models.CharField(max_length=1, blank=True, null=True)
    qty_bbc = models.IntegerField(blank=True, null=True)
    rate_bbc = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    lbc_charge_bbc = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    is_ioa = models.CharField(max_length=1, blank=True, null=True)
    alt_job_id = models.IntegerField(blank=True, null=True)
    is_quote = models.CharField(max_length=1, blank=True, null=True)
    job_no_add = models.CharField(max_length=7, blank=True, null=True)
    is_att = models.CharField(max_length=1, blank=True, null=True)
    show_comments = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_temp'


class LastPrintComment(models.Model):
    last_print_comment_id = models.AutoField(primary_key=True)
    comment1 = models.TextField(blank=True, null=True)
    comment2 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'last_print_comment'


class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message'


class MessageOp(models.Model):
    message_id = models.IntegerField()
    operator_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'message_op'
        unique_together = (('operator_id', 'message_id'),)


class Operator(models.Model):
    operator_id = models.AutoField(primary_key=True)
    company = models.CharField(max_length=50, blank=True, null=True)
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
    ph_desk = models.CharField(max_length=255, blank=True, null=True)
    rate_code = models.CharField(max_length=255, blank=True, null=True)
    scanner_no1 = models.CharField(max_length=255, blank=True, null=True)
    scanner_no2 = models.CharField(max_length=255, blank=True, null=True)
    scanner_no3 = models.CharField(max_length=255, blank=True, null=True)
    scanner_no4 = models.CharField(max_length=255, blank=True, null=True)
    scanner_phone_no1 = models.CharField(max_length=255, blank=True, null=True)
    scanner_phone_no2 = models.CharField(max_length=255, blank=True, null=True)
    scanner_phone_no3 = models.CharField(max_length=255, blank=True, null=True)
    scanner_phone_no4 = models.CharField(max_length=255, blank=True, null=True)
    scanner_email = models.CharField(max_length=255, blank=True, null=True)
    scanner_charke = models.CharField(max_length=255, blank=True, null=True)
    scanner_charge = models.CharField(max_length=255, blank=True, null=True)
    scanner_mobile_pay = models.CharField(max_length=255, blank=True, null=True)
    mobile_pay = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operator'


class ParcelInvoice(models.Model):
    parcel_invoice = models.AutoField(primary_key=True)
    invoice_no = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    dist_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcel_invoice'


class ParcelJob(models.Model):
    job_id = models.AutoField(primary_key=True)
    purchase_no = models.CharField(max_length=50, blank=True, null=True)
    client_id = models.IntegerField(blank=True, null=True)
    job_no = models.IntegerField(blank=True, null=True)
    invoice_no = models.CharField(max_length=50, blank=True, null=True)
    foreign_order_no = models.CharField(max_length=30, blank=True, null=True)
    order_date = models.DateTimeField(blank=True, null=True)
    change_date = models.DateField(blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    confirmed = models.CharField(max_length=1, blank=True, null=True)
    finished = models.CharField(max_length=1, blank=True, null=True)
    cancelled = models.CharField(max_length=1, blank=True, null=True)
    is_ioa = models.CharField(max_length=1, blank=True, null=True)
    gst = models.FloatField(blank=True, null=True)
    fuel_surcharge = models.FloatField(blank=True, null=True)
    ordered_by = models.CharField(max_length=30, blank=True, null=True)
    order_no = models.CharField(max_length=255, blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField(blank=True, null=True)
    branch_id1 = models.IntegerField(blank=True, null=True)
    branch_id2 = models.IntegerField(blank=True, null=True)
    branch_id3 = models.IntegerField(blank=True, null=True)
    is_random = models.IntegerField(blank=True, null=True)
    is_odd = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcel_job'


class ParcelJobRate(models.Model):
    parcel_job_rate_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=3, blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)
    red_rate_pickup = models.FloatField(blank=True, null=True)
    red_rate_deliv = models.FloatField(blank=True, null=True)
    sell_rate = models.FloatField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    distr_payment_deliv = models.FloatField(blank=True, null=True)
    distr_payment_pickup = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcel_job_rate'


class ParcelJobRoute(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    job_id = models.IntegerField(blank=True, null=True)
    ticket_no = models.IntegerField(blank=True, null=True)
    parcel_run_id = models.IntegerField(blank=True, null=True)
    is_redeemed_p = models.IntegerField(db_column='is_redeemed_P', blank=True, null=True)  # Field name made lowercase.
    is_redeemed_d = models.IntegerField(db_column='is_redeemed_D', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=3, blank=True, null=True)
    is_random = models.IntegerField(blank=True, null=True)
    dist_id = models.IntegerField(blank=True, null=True)
    route_id = models.IntegerField(blank=True, null=True)
    contractor_id = models.IntegerField(blank=True, null=True)
    red_rate_pickup = models.FloatField(blank=True, null=True)
    red_rate_deliv = models.FloatField(blank=True, null=True)
    distr_payment_deliv = models.FloatField(blank=True, null=True)
    distr_payment_pickup = models.FloatField(blank=True, null=True)
    dummy = models.IntegerField(blank=True, null=True)
    has_photo = models.CharField(max_length=2, blank=True, null=True)
    has_signature = models.CharField(max_length=2, blank=True, null=True)
    has_atl = models.CharField(max_length=2, blank=True, null=True)
    has_ctc = models.CharField(max_length=2, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    suburb = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    postcode = models.CharField(max_length=5, blank=True, null=True)
    is_mobile = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcel_job_route'


class ParcelJobRouteLog(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    ticket_id = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    who = models.CharField(max_length=255, blank=True, null=True)
    what = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcel_job_route_log'


class ParcelJobRoutePre(models.Model):
    ticket_pre_id = models.AutoField(primary_key=True)
    parcel_run_pre_id = models.IntegerField(blank=True, null=True)
    ticket_no = models.CharField(max_length=20, blank=True, null=True)
    is_random = models.IntegerField(blank=True, null=True)
    contractor_id = models.IntegerField(blank=True, null=True)
    is_processed = models.IntegerField(blank=True, null=True)
    route_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcel_job_route_pre'


class ParcelJobTicket(models.Model):
    parcel_job_ticket_id = models.AutoField(primary_key=True)
    job_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=3, blank=True, null=True)
    start = models.IntegerField(blank=True, null=True)
    end = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcel_job_ticket'


class ParcelOldRed(models.Model):
    ticket_number = models.CharField(db_column='Ticket_Number', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_sold = models.CharField(db_column='Date_Sold', max_length=20, blank=True, null=True)  # Field name made lowercase.
    customer = models.IntegerField(db_column='Customer', blank=True, null=True)  # Field name made lowercase.
    pickup = models.CharField(db_column='Pickup', max_length=255, blank=True, null=True)  # Field name made lowercase.
    delivery = models.CharField(db_column='Delivery', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ticket_no = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=5, blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcel_old_red'


class ParcelOldUnred(models.Model):
    ticket_number = models.CharField(db_column='Ticket_Number', max_length=15, blank=True, null=True)  # Field name made lowercase.
    date_sold = models.CharField(db_column='Date_Sold', max_length=20, blank=True, null=True)  # Field name made lowercase.
    customer = models.IntegerField(db_column='Customer', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=5, blank=True, null=True)
    ticket_no = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcel_old_unred'


class ParcelPrice(models.Model):
    oid = models.AutoField(primary_key=True)
    client_id = models.IntegerField(blank=True, null=True)
    sell_rate = models.FloatField(blank=True, null=True)
    qty_per_book = models.IntegerField(blank=True, null=True)
    type_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcel_price'


class ParcelRates(models.Model):
    parcel_rate_id = models.AutoField(primary_key=True)
    red_rate_pickup = models.FloatField(blank=True, null=True)
    red_rate_deliv = models.FloatField(blank=True, null=True)
    distr_payment_deliv = models.FloatField(blank=True, null=True)
    distr_payment_pickup = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=3, blank=True, null=True)
    sell_rate_std = models.FloatField(blank=True, null=True)
    sell_rate_disc = models.FloatField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    qty_per_book = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcel_rates'


class ParcelRun(models.Model):
    parcel_run_id = models.AutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    dist_id = models.IntegerField(blank=True, null=True)
    run = models.IntegerField(blank=True, null=True)
    route_id = models.IntegerField(blank=True, null=True)
    contractor_id = models.IntegerField(blank=True, null=True)
    invoice_no = models.IntegerField(blank=True, null=True)
    exp_no_tickets = models.IntegerField(blank=True, null=True)
    red_ticket_count = models.IntegerField(blank=True, null=True)
    real_date = models.DateTimeField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    actual = models.IntegerField(blank=True, null=True)
    dummy = models.IntegerField(blank=True, null=True)
    batch_no = models.IntegerField(blank=True, null=True)
    mobile_batch = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcel_run'


class ParcelRunPre(models.Model):
    parcel_run_pre_id = models.AutoField(primary_key=True)
    dist_id = models.IntegerField(blank=True, null=True)
    contractor_id = models.IntegerField(blank=True, null=True)
    route_id = models.IntegerField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)
    real_date = models.DateTimeField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    actual = models.IntegerField(blank=True, null=True)
    is_processed = models.IntegerField(blank=True, null=True)
    parcel_run_id = models.IntegerField(blank=True, null=True)
    batch_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcel_run_pre'


class ParcelThReceipt(models.Model):
    parcel_th_receipt_id = models.AutoField(primary_key=True)
    branch_id = models.IntegerField(blank=True, null=True)
    supplier = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcel_th_receipt'


class ParcelTicketNote(models.Model):
    parcel_ticket_note_id = models.AutoField(primary_key=True)
    start = models.IntegerField(blank=True, null=True)
    end = models.IntegerField(blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcel_ticket_note'


class ParcelTicketTh(models.Model):
    parcel_ticket_th_id = models.AutoField(primary_key=True)
    parcel_th_receipt_id = models.IntegerField(blank=True, null=True)
    start = models.IntegerField(blank=True, null=True)
    end = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=3, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcel_ticket_th'


class ParcelTicketTypes(models.Model):
    oid = models.AutoField(primary_key=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    colour = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcel_ticket_types'


class ParcelTickets(models.Model):
    oid = models.AutoField(primary_key=True)
    job_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    ticket_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcel_tickets'


class PayoutInvoiceNo(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    max_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payout_invoice_no'


class Pod(models.Model):
    date = models.DateField(blank=True, null=True)
    pod_no = models.CharField(max_length=20, blank=True, null=True)
    ticket_no = models.CharField(max_length=20, blank=True, null=True)
    staff_id = models.IntegerField(blank=True, null=True)
    staff_claim_id = models.IntegerField(blank=True, null=True)
    staff_app_claim_id = models.IntegerField(blank=True, null=True)
    is_claim = models.IntegerField()
    courier_id = models.IntegerField(blank=True, null=True)
    ticket_id = models.IntegerField(blank=True, null=True)
    dist_id = models.IntegerField(blank=True, null=True)
    contr_id = models.IntegerField(blank=True, null=True)
    ticket_type = models.CharField(max_length=3, blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    branch = models.CharField(max_length=100, blank=True, null=True)
    sendfrom = models.CharField(max_length=100, blank=True, null=True)
    contname = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    fax = models.CharField(max_length=100, blank=True, null=True)
    yourticket = models.CharField(max_length=100, blank=True, null=True)
    parcelleft = models.CharField(max_length=255, blank=True, null=True)
    parceldate = models.DateField(blank=True, null=True)
    contc = models.CharField(max_length=5, blank=True, null=True)
    cresponse = models.TextField(blank=True, null=True)
    addresseename = models.CharField(max_length=100, blank=True, null=True)
    parceladdr = models.CharField(max_length=100, blank=True, null=True)
    naturecontents = models.CharField(max_length=100, blank=True, null=True)
    whosent = models.CharField(max_length=100, blank=True, null=True)
    initenquiry = models.CharField(max_length=100, blank=True, null=True)
    problem = models.TextField(blank=True, null=True)
    email2 = models.CharField(max_length=100, blank=True, null=True)
    claim_status_id = models.IntegerField(blank=True, null=True)
    ticket_d_id = models.IntegerField(blank=True, null=True)
    ticket_p_id = models.IntegerField(blank=True, null=True)
    ccompany = models.CharField(max_length=100, blank=True, null=True)
    sentfrom = models.CharField(max_length=100, blank=True, null=True)
    couralticket = models.CharField(max_length=100, blank=True, null=True)
    addresseephone = models.CharField(max_length=100, blank=True, null=True)
    sendcopytome = models.CharField(max_length=100, blank=True, null=True)
    claim_courier_no = models.CharField(max_length=100, blank=True, null=True)
    claim_courier_person = models.CharField(max_length=100, blank=True, null=True)
    claim_reason = models.CharField(max_length=255, blank=True, null=True)
    claim_amount = models.FloatField(blank=True, null=True)
    claim_description = models.TextField(blank=True, null=True)
    claim_decision_reason = models.CharField(max_length=255, blank=True, null=True)
    claim_courier_advise = models.DateField(blank=True, null=True)
    claim_courier_advise_how = models.CharField(max_length=255, blank=True, null=True)
    claim_coural_staff_id = models.IntegerField(blank=True, null=True)
    claim_coural_approval_id = models.IntegerField(blank=True, null=True)
    claim_contr_invoice_date = models.DateField(blank=True, null=True)
    claim_contr_invoice_amount = models.FloatField(blank=True, null=True)
    claim_ticket_picture = models.CharField(max_length=255, blank=True, null=True)
    claim_item_picture = models.CharField(max_length=255, blank=True, null=True)
    do_id = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    time_limit_pod = models.DateField(blank=True, null=True)
    time_damage_claim = models.DateField(blank=True, null=True)
    time_lossd_claim = models.DateField(blank=True, null=True)
    claim_date = models.DateField(blank=True, null=True)
    claim_type_id = models.IntegerField(blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    pod_web_id = models.IntegerField(blank=True, null=True)
    contr_name = models.CharField(max_length=100, blank=True, null=True)
    pod_prev_req = models.IntegerField(blank=True, null=True)
    pod_ref_no = models.CharField(max_length=100, blank=True, null=True)
    pod_id = models.AutoField(primary_key=True)
    claim_contr_liable = models.IntegerField(blank=True, null=True)
    is_archived = models.IntegerField()
    road = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    rd = models.CharField(max_length=255, blank=True, null=True)
    route_id = models.IntegerField(blank=True, null=True)
    dropoff_id = models.IntegerField(blank=True, null=True)
    ticket_no_search = models.TextField(blank=True, null=True)
    is_flagged = models.IntegerField(blank=True, null=True)
    initials = models.CharField(max_length=20, blank=True, null=True)
    days_last_action = models.IntegerField(blank=True, null=True)
    last_action_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pod'


class PodAction(models.Model):
    action_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pod_action'


class PodActionLog(models.Model):
    action_log_id = models.AutoField(primary_key=True)
    staff_id = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)
    pod_id = models.IntegerField(blank=True, null=True)
    subject = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pod_action_log'


class PodActivity(models.Model):
    activity_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'pod_activity'


class PodActivityLog(models.Model):
    activity_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'pod_activity_log'


class PodClaimStatus(models.Model):
    claim_status_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pod_claim_status'


class PodClaimTyp(models.Model):
    claim_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pod_claim_typ'


class PodMaxNo(models.Model):
    max_no_id = models.AutoField(primary_key=True)
    value = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pod_max_no'


class PodStaff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pod_staff'


class PodStaffActionAss(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pod_staff_action_ass'


class PodStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pod_status'


class PodTicket(models.Model):
    oid = models.AutoField(primary_key=True)
    ticket_id = models.IntegerField(blank=True, null=True)
    pickup_date = models.DateField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    redeemed_op = models.IntegerField(blank=True, null=True)
    delivered_op = models.IntegerField(blank=True, null=True)
    seq = models.IntegerField(blank=True, null=True)
    pod_id = models.IntegerField(blank=True, null=True)
    ticket_no = models.CharField(max_length=50, blank=True, null=True)
    ticket_type = models.CharField(max_length=3, blank=True, null=True)
    ticket_no_courier = models.CharField(max_length=50, blank=True, null=True)
    is_primary = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pod_ticket'


class PodTicketCourier(models.Model):
    oid = models.AutoField(primary_key=True)
    ticket_no = models.CharField(max_length=50, blank=True, null=True)
    pod_id = models.IntegerField(blank=True, null=True)
    seq = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pod_ticket_courier'


class RegistrationRegistrationprofile(models.Model):
    user_id = models.IntegerField(unique=True)
    activation_key = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'registration_registrationprofile'


class Route(models.Model):
    route_id = models.AutoField(primary_key=True)
    island = models.CharField(max_length=3, blank=True, null=True)
    region = models.CharField(max_length=30, blank=True, null=True)
    area = models.CharField(max_length=30, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    external = models.CharField(max_length=11, blank=True, null=True)
    no_ticket_header = models.CharField(max_length=1)
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
    is_hidden = models.CharField(max_length=1, blank=True, null=True)
    num_nzfw = models.IntegerField(blank=True, null=True)
    rmt = models.IntegerField(blank=True, null=True)
    rm_rr = models.IntegerField(blank=True, null=True)
    rm_f = models.IntegerField(blank=True, null=True)
    rm_d = models.IntegerField(blank=True, null=True)
    code_base = models.CharField(max_length=100, blank=True, null=True)
    code_rd = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'route'


class RouteAff(models.Model):
    route_aff_id = models.AutoField(primary_key=True)
    route_id = models.IntegerField()
    dist_id = models.IntegerField(blank=True, null=True)
    subdist_id = models.IntegerField(blank=True, null=True)
    contractor_id = models.IntegerField(blank=True, null=True)
    dropoff_id = models.IntegerField(blank=True, null=True)
    app_date = models.DateField(blank=True, null=True)
    stop_date = models.DateField(blank=True, null=True)
    env_dist_id = models.IntegerField(blank=True, null=True)
    env_contractor_id = models.IntegerField(blank=True, null=True)
    pc_dist_id = models.IntegerField(blank=True, null=True)
    env_subdist_id = models.IntegerField(blank=True, null=True)
    pc_contractor_id = models.IntegerField(blank=True, null=True)
    env_dropoff_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'route_aff'


class RouteBu(models.Model):
    route_id = models.IntegerField()
    island = models.CharField(max_length=3, blank=True, null=True)
    region = models.CharField(max_length=30, blank=True, null=True)
    area = models.CharField(max_length=30, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    external = models.CharField(max_length=11, blank=True, null=True)
    no_ticket_header = models.CharField(max_length=1)
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
    is_hidden = models.CharField(max_length=1, blank=True, null=True)
    num_nzfw = models.IntegerField(blank=True, null=True)
    rmt = models.IntegerField(blank=True, null=True)
    rm_rr = models.IntegerField(blank=True, null=True)
    rm_f = models.IntegerField(blank=True, null=True)
    rm_d = models.IntegerField(blank=True, null=True)
    code_base = models.CharField(max_length=100, blank=True, null=True)
    code_rd = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'route_bu'


class RouteOldNum(models.Model):
    route_old_num_id = models.AutoField(primary_key=True)
    backup_date = models.DateField(blank=True, null=True)
    operator_id = models.IntegerField(blank=True, null=True)
    distributor = models.TextField(blank=True, null=True)
    route_id = models.IntegerField()
    dist_id = models.IntegerField(blank=True, null=True)
    subdist_id = models.IntegerField(blank=True, null=True)
    contractor_id = models.IntegerField(blank=True, null=True)
    island = models.CharField(max_length=3, blank=True, null=True)
    region = models.CharField(max_length=30, blank=True, null=True)
    area = models.CharField(max_length=30, blank=True, null=True)
    code = models.CharField(max_length=30, blank=True, null=True)
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
    external = models.CharField(max_length=11, blank=True, null=True)
    seq_region = models.IntegerField(blank=True, null=True)
    seq_area = models.IntegerField(blank=True, null=True)
    seq_code = models.IntegerField(blank=True, null=True)
    num_nzfw = models.IntegerField(blank=True, null=True)
    num_spare = models.IntegerField(blank=True, null=True)
    is_hidden = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'route_old_num'


class ScheduleMailSendOut(models.Model):
    config = models.TextField(blank=True, null=True)
    exec_field = models.DateTimeField(db_column='exec', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    status = models.IntegerField(blank=True, null=True)
    dtt = models.DateTimeField()
    loch = models.IntegerField(blank=True, null=True)
    oid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'schedule_mail_send_out'


class SendReport(models.Model):
    send_report_id = models.AutoField(primary_key=True)
    jobs = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    dist_id = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    final_date = models.DateField(blank=True, null=True)
    show_regular = models.CharField(max_length=1, blank=True, null=True)
    show_casual = models.CharField(max_length=1, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'send_report'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    passwd = models.CharField(max_length=50, blank=True, null=True)
    security_lev = models.IntegerField(blank=True, null=True)
    page_main = models.CharField(max_length=1, blank=True, null=True)
    page_procjob = models.CharField(max_length=1, blank=True, null=True)
    page_useradmin = models.CharField(max_length=1, blank=True, null=True)
    page_routeadmin = models.CharField(max_length=1, blank=True, null=True)
    page_clientadmin = models.CharField(max_length=1, blank=True, null=True)
    page_addradmin = models.CharField(max_length=1, blank=True, null=True)
    page_opadmin = models.CharField(max_length=1, blank=True, null=True)
    page_reports = models.CharField(max_length=1, blank=True, null=True)
    page_rep_revenue = models.CharField(max_length=1, blank=True, null=True)
    page_invoice = models.CharField(max_length=1, blank=True, null=True)
    page_parcels = models.CharField(max_length=1, blank=True, null=True)
    page_rep_parcels = models.CharField(max_length=1, blank=True, null=True)
    gst = models.CharField(max_length=1, blank=True, null=True)
    full_name = models.TextField(blank=True, null=True)
    page_rep_old = models.CharField(max_length=1, blank=True, null=True)
    haul_island = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserDefaults(models.Model):
    user_default_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    value_date = models.DateField(blank=True, null=True)
    value_int = models.IntegerField(blank=True, null=True)
    value_string = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_defaults'


class WebParcelpickup(models.Model):
    pickup_no = models.CharField(max_length=255)
    status = models.CharField(max_length=10)
    dtt = models.DateField()
    rd = models.CharField(max_length=1024)
    ccompany = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    contname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    sendername = models.CharField(max_length=255)
    senderaddress = models.CharField(max_length=255)
    parcelquantity = models.IntegerField()
    parcelleft = models.CharField(max_length=255)
    parceldescr = models.CharField(max_length=255)
    yourticket = models.CharField(max_length=255)
    receivername = models.CharField(max_length=255)
    cticket = models.TextField()
    hsh = models.CharField(max_length=255)
    contractor_id = models.IntegerField()
    route_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'web_parcelpickup'
