# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_auto_20140924_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operation',
            name='total',
        ),
    ]
