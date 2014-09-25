# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0009_offer_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='percent_cashback',
            field=models.DecimalField(default=0, verbose_name='Percentual de CashBack', max_digits=10, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='offer',
            field=models.ForeignKey(related_name=b'images', to='offer.Offer'),
        ),
    ]
