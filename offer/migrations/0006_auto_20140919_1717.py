# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0005_auto_20140919_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='affiliate',
            field=models.ForeignKey(verbose_name='Franqueado', blank=True, to='account.Affiliate', null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='percent_by_affiliate',
            field=models.DecimalField(null=True, verbose_name='Percentual do afiliado', max_digits=10, decimal_places=2, blank=True),
        ),
    ]
