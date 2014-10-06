# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0011_offer_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='city',
        ),
    ]
