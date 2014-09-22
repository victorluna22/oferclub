# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_operation'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='total',
            field=models.DecimalField(default=0, verbose_name='total', max_digits=10, decimal_places=2),
            preserve_default=False,
        ),
    ]
