# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0009_remove_operation_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='description',
            field=models.CharField(default='', max_length=255, verbose_name='Descri\xe7\xe3o'),
            preserve_default=False,
        ),
    ]
