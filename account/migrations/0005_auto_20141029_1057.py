# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_oferclubuser_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='complement',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
