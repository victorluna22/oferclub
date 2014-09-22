# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='address',
            field=models.ForeignKey(verbose_name='endere\xe7o', blank=True, to='account.Address', null=True),
        ),
    ]
