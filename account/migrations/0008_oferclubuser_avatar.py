# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_remove_address_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferclubuser',
            name='avatar',
            field=models.ImageField(default='', upload_to=b'usuario/', verbose_name='Avatar'),
            preserve_default=False,
        ),
    ]
