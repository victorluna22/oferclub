# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0010_operation_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='code_pagseguro',
            field=models.CharField(max_length=255, null=True, verbose_name='C\xf3digo PagSeguro', blank=True),
            preserve_default=True,
        ),
    ]
