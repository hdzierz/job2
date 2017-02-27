# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-19 20:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_files', '0007_clientprice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='old_id',
            new_name='old_address_id',
        ),
        migrations.AddField(
            model_name='address',
            name='parent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mother', to='master_files.Address'),
            preserve_default=False,
        ),
    ]
