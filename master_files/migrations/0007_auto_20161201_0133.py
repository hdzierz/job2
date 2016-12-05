# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 01:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_files', '0006_auto_20161201_0126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='salutation',
        ),
        migrations.RemoveField(
            model_name='address',
            name='salutation2',
        ),
        migrations.AddField(
            model_name='address',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='old_operator_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
