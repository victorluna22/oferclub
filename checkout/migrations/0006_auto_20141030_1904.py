# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20141030_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.DecimalField(verbose_name='valor pago', max_digits=10, decimal_places=2),
        ),
    ]
