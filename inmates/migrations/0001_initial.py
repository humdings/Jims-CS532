# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street_number', models.IntegerField()),
                ('street_name', models.CharField(max_length=100)),
                ('apartment_number', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(default=b'CA', max_length=30)),
                ('zip_code', models.IntegerField()),
                ('country', models.CharField(default=b'USA', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Inmate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('aliases', models.CharField(max_length=5000)),
                ('address', models.ForeignKey(to='inmates.Address')),
            ],
        ),
    ]
