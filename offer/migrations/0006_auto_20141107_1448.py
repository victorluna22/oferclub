# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0005_offer_shipping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='shipping',
            field=models.BooleanField(default=0, verbose_name='Cobra Frete'),
        ),
    ]
