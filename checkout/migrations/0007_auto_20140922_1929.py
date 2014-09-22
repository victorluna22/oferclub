# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_operation_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Quantidade'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.PositiveSmallIntegerField(default=2, null=True, verbose_name='situa\xe7\xe3o', blank=True, choices=[(0, 'Aprovada'), (1, 'Negada'), (2, 'Em An\xe1lise')]),
        ),
    ]
