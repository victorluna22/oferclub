# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20140919_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='order',
            field=models.ForeignKey(related_name=b'get_coupons', default=2, to='checkout.Order'),
            preserve_default=False,
        ),
    ]
