# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0004_auto_20140918_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='filial',
            field=models.ForeignKey(related_name=b'offers', to='account.Filial'),
        ),
        migrations.AlterField(
            model_name='option',
            name='offer',
            field=models.ForeignKey(related_name=b'options', to='offer.Offer'),
        ),
    ]
