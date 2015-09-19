# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inmates', '0002_auto_20150916_2349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inmate',
            old_name='address',
            new_name='temporary_address',
        ),
    ]
