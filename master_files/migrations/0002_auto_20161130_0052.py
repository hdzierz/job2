# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 00:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_files', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
