# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-15 00:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_files', '0005_remove_address_is_alt_dropoff'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdressSupp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255)),
                ('po_box', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('post_code', models.CharField(max_length=255)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_files.Address')),
            ],
        ),
        migrations.CreateModel(
            name='CfgAdressSuppType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.AddField(
            model_name='adresssupp',
            name='typ',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_files.CfgAdressSuppType'),
        ),
    ]
