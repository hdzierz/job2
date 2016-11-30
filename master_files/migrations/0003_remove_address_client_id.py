# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_files', '0002_auto_20161130_0052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='client_id',
        ),
    ]
