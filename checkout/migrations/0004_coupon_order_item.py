# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='order_item',
            field=models.ForeignKey(related_name=b'cupons', default=4, to='checkout.OrderItem'),
            preserve_default=False,
        ),
    ]
