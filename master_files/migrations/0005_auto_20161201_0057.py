# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 00:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master_files', '0004_config'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='is_linehaul',
        ),
        migrations.RemoveField(
            model_name='client',
            name='is_operator',
        ),
    ]
