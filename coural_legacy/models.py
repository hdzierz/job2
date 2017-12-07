# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class LCRoute(models.Model):
    route_id = models.AutoField(primary_key=True)
    island = models.TextField(blank=True, null=True)
    area = models.TextField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
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
    #code_basei = models.CharField(max_length=255)
    code_rd = models.CharField(max_length=255)
    
    class Meta:
        managed = False
        db_table = 'route'


class LCAddress(models.Model):
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


class LCAddressCopy(models.Model):
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


class LCAuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class LCAuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class LCAuthPermission(models.Model):
    name = models.CharField(max_length=50)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class LCAuthUser(models.Model):
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


class LCAuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class LCAuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class LCBranch(models.Model):
    branch_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'branch'


class LCClient(models.Model):
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


class LCClientBranch(models.Model):
    client_branch_id = models.AutoField(primary_key=True)
    client_id = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_branch'


class LCClientPrice(models.Model):
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


class LCClientPub(models.Model):
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


class LCClientPubs(models.Model):
    client_pub_id = models.AutoField(primary_key=True)
    client_id = models.IntegerField()
    publication = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_pubs'


class LCConfig(models.Model):
    config_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    value = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'config'


class LCControlHistory(models.Model):
    control_history_id = models.AutoField(primary_key=True)
    page = models.TextField(blank=True, null=True)
    request = models.TextField(blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'control_history'


class LCControlLogin(models.Model):
    control_login_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    passwd = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'control_login'


class LCCurrentJobScreen(models.Model):
    current_job_screen_id = models.AutoField(primary_key=True)
    publication = models.TextField(blank=True, null=True)
    client_id = models.IntegerField(blank=True, null=True)
    job_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'current_job_screen'


class LCDjangoAdminLog(models.Model):
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


class LCDjangoContentType(models.Model):
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class LCDjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class LCDjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class LCEmailLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    time_point = models.DateTimeField()
    error_count = models.IntegerField(blank=True, null=True)
    error_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_log'


class LCHoward(models.Model):
    job_id = models.IntegerField(blank=True, null=True)
    ticket_no = models.IntegerField(blank=True, null=True)
    is_redeemed_d = models.IntegerField(db_column='is_redeemed_D', blank=True, null=True)  # Field name made lowercase.
    order_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'howard'


class LCImportC(models.Model):
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


class LCInvoice(models.Model):
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


class LCInvoiceArchive(models.Model):
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


class LCJob(models.Model):
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
    qty_per_bundle_ni = models.IntegerField(blank=True, null=True)
    qty_per_bundle_si = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job'


class LCJobArchive(models.Model):
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


class LCJobCopy(models.Model):
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


class LCJobHoward(models.Model):
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


class LCJobRoute(models.Model):
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


class LCJobRouteArchive(models.Model):
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


class LCJobRouteNew(models.Model):
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


class LCJobRouteTemp(models.Model):
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


class LCJobTemp(models.Model):
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


class LCLastPrintComment(models.Model):
    last_print_comment_id = models.AutoField(primary_key=True)
    comment1 = models.TextField(blank=True, null=True)
    comment2 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'last_print_comment'


class LCLbmClient(models.Model):
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
        db_table = 'lbm_client'


class LCMessage(models.Model):
    message_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message'


class LCMessageOp(models.Model):
    message_id = models.IntegerField()
    operator_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'message_op'
        unique_together = (('operator_id', 'message_id'),)


class LCOperator(models.Model):
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

    class Meta:
        managed = False
        db_table = 'operator'


class LCParcelInvoice(models.Model):
    parcel_invoice = models.AutoField(primary_key=True)
    invoice_no = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    dist_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcel_invoice'


class LCParcelJob(models.Model):
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


class LCParcelJobRate(models.Model):
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


class LCParcelJobRoute(models.Model):
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
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    acc = models.FloatField(blank=True, null=True)
    is_ofd = models.IntegerField(blank=True, null=True)
    is_dmg = models.IntegerField(blank=True, null=True)
    dev_opt = models.CharField(max_length=20, blank=True, null=True)
    dev_drl = models.CharField(max_length=20, blank=True, null=True)
    notes = models.CharField(max_length=100, blank=True, null=True)
    org = models.IntegerField(blank=True, null=True)
    dtt = models.DateTimeField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    distr_payment_pickup_mobile = models.FloatField(blank=True, null=True)
    distr_payment_deliv_mobile = models.FloatField(blank=True, null=True)
    checked = models.IntegerField(blank=True, null=True)
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'parcel_job_route'


class LCParcelJobRouteLog(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    ticket_id = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    who = models.CharField(max_length=255, blank=True, null=True)
    what = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parcel_job_route_log'


class LCParcelJobRoutePre(models.Model):
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


class LCParcelRun(models.Model):
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


class LCCRouteAff(models.Model):
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

