# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_files', '0009_auto_20161219_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='post_code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]