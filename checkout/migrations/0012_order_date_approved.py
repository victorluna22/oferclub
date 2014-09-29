# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0011_order_code_pagseguro'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_approved',
            field=models.DateTimeField(null=True, verbose_name='Aprovado em', blank=True),
            preserve_default=True,
        ),
    ]
