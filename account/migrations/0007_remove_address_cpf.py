# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20141030_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='cpf',
        ),
    ]
