# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inmates', '0003_auto_20150917_0001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inmate',
            name='temporary_address',
        ),
        migrations.AddField(
            model_name='address',
            name='inmate',
            field=models.ForeignKey(default=0, to='inmates.Inmate'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(default=b'USA', max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(default=b'CA', max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='street_name',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='street_number',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.IntegerField(blank=True),
        ),
    ]
