# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0008_auto_20141111_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='slug',
            field=models.SlugField(unique=True, max_length=255, blank=True),
        ),
    ]
