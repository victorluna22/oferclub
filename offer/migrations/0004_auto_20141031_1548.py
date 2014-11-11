# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0003_auto_20141030_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='cep_delivery',
        ),
        migrations.AddField(
            model_name='offer',
            name='cep_delivery',
            field=models.CharField(max_length=9, null=True, verbose_name='CEP de Origem', blank=True),
            preserve_default=True,
        ),
    ]
