# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20141029_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
