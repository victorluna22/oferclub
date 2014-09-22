# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0003_auto_20140918_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='offer',
            name='regulation',
            field=tinymce.models.HTMLField(),
        ),
    ]
