# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inmates', '0005_auto_20150919_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inmate',
            name='smt',
        ),
        migrations.AddField(
            model_name='inmate',
            name='scars_marks_tattoos',
            field=models.TextField(null=True, blank=True),
        ),
    ]
