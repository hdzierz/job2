# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 23:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lbm', '0007_remove_route_code_rd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='code',
        ),
    ]