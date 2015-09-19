# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inmates', '0004_auto_20150917_0048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='inmate',
        ),
        migrations.AddField(
            model_name='inmate',
            name='alt_phone_number',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inmate',
            name='apartment_number',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inmate',
            name='birth_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inmate',
            name='city',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inmate',
            name='country',
            field=models.CharField(default=b'USA', max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inmate',
            name='phone_number',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inmate',
            name='sex',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inmate',
            name='smt',
            field=models.TextField(help_text=b'Scars, marks, and tattoos', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inmate',
            name='social_secutity_number',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inmate',
            name='state',
            field=models.CharField(default=b'CA', max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inmate',
            name='street_name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inmate',
            name='street_number',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inmate',
            name='temporary_apartment_number',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inmate',
            name='temporary_city',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inmate',
            name='temporary_country',
            field=models.CharField(default=b'USA', max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inmate',
            name='temporary_state',
            field=models.CharField(default=b'CA', max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inmate',
            name='temporary_street_name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inmate',
            name='temporary_street_number',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inmate',
            name='temporary_zip_code',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inmate',
            name='zip_code',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='inmate',
            name='aliases',
            field=models.CharField(max_length=5000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='inmate',
            name='middle_name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
