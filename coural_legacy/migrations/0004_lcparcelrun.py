# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coural_legacy', '0003_lcroute'),
    ]

    operations = [
        migrations.CreateModel(
            name='LCParcelRun',
            fields=[
                ('parcel_run_id', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('dist_id', models.IntegerField(null=True, blank=True)),
                ('run', models.IntegerField(null=True, blank=True)),
                ('route_id', models.IntegerField(null=True, blank=True)),
                ('contractor_id', models.IntegerField(null=True, blank=True)),
                ('invoice_no', models.IntegerField(null=True, blank=True)),
                ('exp_no_tickets', models.IntegerField(null=True, blank=True)),
                ('red_ticket_count', models.IntegerField(null=True, blank=True)),
                ('real_date', models.DateTimeField(null=True, blank=True)),
                ('user_id', models.IntegerField(null=True, blank=True)),
                ('actual', models.IntegerField(null=True, blank=True)),
                ('dummy', models.IntegerField(null=True, blank=True)),
                ('batch_no', models.IntegerField(null=True, blank=True)),
                ('mobile_batch', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'db_table': 'parcel_run',
                'managed': False,
            },
        ),
    ]
