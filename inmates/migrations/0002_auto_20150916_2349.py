# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inmates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='apartment_number',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='inmate',
            name='aliases',
            field=models.CharField(max_length=5000, blank=True),
        ),
        migrations.AlterField(
            model_name='inmate',
            name='middle_name',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
