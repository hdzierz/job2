# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_files', '0011_address_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='email',
            field=models.EmailField(default='howard.coural.co.nz', max_length=254),
        ),
    ]