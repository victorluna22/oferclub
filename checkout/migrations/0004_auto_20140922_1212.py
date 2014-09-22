# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0008_auto_20140922_1212'),
        ('checkout', '0003_coupon_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='option',
        ),
        migrations.AddField(
            model_name='order',
            name='option',
            field=models.ForeignKey(related_name=b'orders', default='', to='offer.Option'),
            preserve_default=False,
        ),
    ]
