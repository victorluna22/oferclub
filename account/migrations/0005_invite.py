# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_partner_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name='E-mail')),
                ('invite_date', models.DateTimeField(auto_now_add=True)),
                ('accept_date', models.DateTimeField(null=True, blank=True)),
                ('invited_user', models.ForeignKey(related_name=b'invited', blank=True, to='account.OferClubUser', null=True)),
                ('user', models.ForeignKey(to='account.OferClubUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
