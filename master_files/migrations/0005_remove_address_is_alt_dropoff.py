# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-13 08:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master_files', '0004_auto_20161213_0252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='is_alt_dropoff',
        ),
    ]
