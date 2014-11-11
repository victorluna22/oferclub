# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20141111_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='filial',
            name='latitude',
            field=models.CharField(max_length=100, null=True, verbose_name='Latitude', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='filial',
            name='longitude',
            field=models.CharField(max_length=100, null=True, verbose_name='Latitude', blank=True),
            preserve_default=True,
        ),
    ]
