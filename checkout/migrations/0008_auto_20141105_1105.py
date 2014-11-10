# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_auto_20141104_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='name_consumer',
            field=models.CharField(max_length=200, null=True, verbose_name='nome completo', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(related_name=b'itens', to='checkout.Order'),
        ),
    ]
