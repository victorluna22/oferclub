# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='order',
        ),
        migrations.RemoveField(
            model_name='order',
            name='name_consumer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='option',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='send_gift',
        ),
    ]
