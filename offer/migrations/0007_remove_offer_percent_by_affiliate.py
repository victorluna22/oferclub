# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0006_auto_20140919_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='percent_by_affiliate',
        ),
    ]
