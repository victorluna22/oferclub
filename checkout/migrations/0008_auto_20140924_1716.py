# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_auto_20140922_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='date_consumed',
            field=models.DateTimeField(null=True, verbose_name='Consumido em', blank=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='name_consumer',
            field=models.CharField(max_length=200, null=True, verbose_name='nome completo', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Quantidade'),
        ),
    ]
