# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0003_auto_20141030_1839'),
        ('checkout', '0002_auto_20141030_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_consumer', models.CharField(max_length=200, null=True, verbose_name='nome completo', blank=True)),
                ('quantity', models.IntegerField(default=1, verbose_name='Quantidade')),
                ('total', models.DecimalField(verbose_name='valor pago', max_digits=10, decimal_places=2)),
                ('option', models.ForeignKey(related_name=b'orders', to='offer.Option')),
                ('order', models.ForeignKey(related_name=b'get_coupons', to='checkout.Order')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
