# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0009_auto_20141111_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='subtitle',
            field=models.CharField(max_length=255, null=True, verbose_name='Sub T\xedtulo', blank=True),
        ),
    ]
