# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20141029_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferclubuser',
            name='address',
            field=models.ManyToManyField(to='account.Address'),
            preserve_default=True,
        ),
    ]
