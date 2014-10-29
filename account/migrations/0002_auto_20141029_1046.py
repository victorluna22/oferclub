# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='city',
        ),
        migrations.AddField(
            model_name='address',
            name='cpf',
            field=models.CharField(default='', max_length=14),
            preserve_default=False,
        ),
    ]
