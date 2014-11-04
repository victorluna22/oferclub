# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_auto_20141030_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='balance',
            field=models.DecimalField(default=0, verbose_name='Saldo usado', max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.DecimalField(default=0, verbose_name='Desconto', max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='shipping',
            field=models.DecimalField(default=0, verbose_name='Frete', max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
    ]
