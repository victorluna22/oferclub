# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='delivery',
            field=models.BooleanField(default=0, verbose_name='Entrega'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='option',
            name='cep_delivery',
            field=models.CharField(max_length=9, null=True, verbose_name='CEP de Origem', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='option',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=10, blank=True, help_text='cm', null=True, verbose_name='Altura'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='option',
            name='length',
            field=models.DecimalField(decimal_places=2, max_digits=10, blank=True, help_text='cm', null=True, verbose_name='Tamanho'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='option',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=10, blank=True, help_text='kg', null=True, verbose_name='Peso'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='option',
            name='width',
            field=models.DecimalField(decimal_places=2, max_digits=10, blank=True, help_text='cm', null=True, verbose_name='Largura'),
            preserve_default=True,
        ),
    ]
