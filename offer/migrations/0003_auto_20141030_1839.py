# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0002_auto_20141029_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=10, blank=True, help_text='min: 2cm', null=True, verbose_name='Altura'),
        ),
        migrations.AlterField(
            model_name='option',
            name='length',
            field=models.DecimalField(decimal_places=2, max_digits=10, blank=True, help_text='min: 16cm', null=True, verbose_name='Tamanho'),
        ),
        migrations.AlterField(
            model_name='option',
            name='width',
            field=models.DecimalField(decimal_places=2, max_digits=10, blank=True, help_text='min: 11cm', null=True, verbose_name='Largura'),
        ),
    ]
