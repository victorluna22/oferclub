# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20140918_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='affiliate',
            name='percent',
            field=models.DecimalField(null=True, verbose_name='Percentual do afiliado', max_digits=10, decimal_places=2, blank=True),
            preserve_default=True,
        ),
    ]
