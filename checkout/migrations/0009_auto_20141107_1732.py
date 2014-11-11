# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20141030_1838'),
        ('checkout', '0008_auto_20141105_1105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='address',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(verbose_name='endere\xe7o', blank=True, to='account.Address', null=True),
            preserve_default=True,
        ),
    ]
