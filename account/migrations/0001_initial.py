# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OferClubAbstractUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('full_name', models.CharField(max_length=200, verbose_name='Nome completo')),
                ('email', models.EmailField(null=True, max_length=254, blank=True, unique=True, verbose_name='Email', db_index=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designa se este usu\xe1rio pode acessar este site admin.', verbose_name='Membro da equipe')),
                ('is_active', models.BooleanField(default=True, help_text='Designa se este usu\xe1rio est\xe1 ativo.Desmarque esta op\xe7\xe3o ao inv\xe9s de deletar a conta.', verbose_name='Ativo')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Criado em')),
                ('slug', models.SlugField(unique=True, max_length=255, editable=False, blank=True)),
            ],
            options={
                'verbose_name': 'usu\xe1rio do Lua de V\xe9u',
                'verbose_name_plural': 'usu\xe1rios do Lua de V\xe9u',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('provider', models.CharField(db_index=True, max_length=20, verbose_name='provedor', choices=[('facebook', 'Facebook')])),
                ('provider_id', models.CharField(max_length=100, verbose_name='id no provedor')),
                ('provider_username', models.CharField(max_length=100, verbose_name='login no provedor')),
                ('oauth_token', models.CharField(max_length=254, verbose_name='oauth token')),
                ('oauth_token_secret', models.CharField(max_length=254, verbose_name='oauth token secret')),
                ('refresh_token', models.CharField(max_length=254, verbose_name='refresh token')),
                ('expires_in', models.DateTimeField(null=True, verbose_name='expira em')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'conta',
                'verbose_name_plural': 'contas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cep', models.CharField(max_length=9)),
                ('street', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=100)),
                ('complement', models.CharField(max_length=100)),
                ('neighborhood', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Affiliate',
            fields=[
                ('oferclubabstractuser_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.CharField(max_length=20, null=True, verbose_name='Telefone', blank=True)),
                ('cellphone', models.CharField(max_length=20, null=True, verbose_name='Celular', blank=True)),
                ('percent', models.DecimalField(null=True, verbose_name='Percentual do afiliado', max_digits=10, decimal_places=2, blank=True)),
                ('owner_name', models.CharField(help_text='Nome do titular', max_length=200, null=True, verbose_name='Nome do Titular', blank=True)),
                ('bank_name', models.CharField(help_text='Nome do banco', max_length=100, null=True, verbose_name='Banco', blank=True)),
                ('agency', models.CharField(help_text='C\xf3digo da ag\xeancia', max_length=100, null=True, verbose_name='Ag\xeancia', blank=True)),
                ('number', models.CharField(help_text='N\xfamero da conta', max_length=100, null=True, verbose_name='Conta', blank=True)),
                ('cpf', models.CharField(help_text='CPF do propriet\xe1rio da conta', max_length=14, null=True, verbose_name='CPF', blank=True)),
            ],
            options={
                'verbose_name': 'Franqueado',
                'verbose_name_plural': 'Franqueados',
            },
            bases=('account.oferclubabstractuser',),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Filial',
            fields=[
                ('oferclubabstractuser_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.CharField(max_length=20, null=True, verbose_name='Telefone', blank=True)),
                ('cellphone', models.CharField(max_length=20, null=True, verbose_name='Celular', blank=True)),
                ('cep', models.CharField(max_length=9, null=True, verbose_name='CEP', blank=True)),
                ('street', models.CharField(max_length=255, null=True, verbose_name='Logradouro', blank=True)),
                ('number_home', models.CharField(max_length=100, null=True, verbose_name='N\xfamero', blank=True)),
                ('complement', models.CharField(max_length=100, null=True, verbose_name='Complemento', blank=True)),
                ('neighborhood', models.CharField(max_length=100, null=True, verbose_name='Bairro', blank=True)),
                ('owner_name', models.CharField(help_text='Nome do titular', max_length=200, null=True, verbose_name='Nome do Titular', blank=True)),
                ('bank_name', models.CharField(help_text='Nome do banco', max_length=100, null=True, verbose_name='Banco', blank=True)),
                ('agency', models.CharField(help_text='C\xf3digo da ag\xeancia', max_length=100, null=True, verbose_name='Ag\xeancia', blank=True)),
                ('number', models.CharField(help_text='N\xfamero da conta', max_length=100, null=True, verbose_name='Conta', blank=True)),
                ('cpf', models.CharField(help_text='CPF do propriet\xe1rio da conta', max_length=14, null=True, verbose_name='CPF', blank=True)),
                ('city', models.ForeignKey(blank=True, to='account.City', null=True)),
            ],
            options={
                'verbose_name': 'Filial',
                'verbose_name_plural': 'Filiais',
            },
            bases=('account.oferclubabstractuser',),
        ),
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name='E-mail')),
                ('invite_date', models.DateTimeField(auto_now_add=True)),
                ('accept_date', models.DateTimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name='E-mail')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('city', models.ForeignKey(verbose_name=b'Cidade', to='account.City')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OferClubUser',
            fields=[
                ('oferclubabstractuser_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('gender', models.CharField(blank=True, max_length=1, null=True, verbose_name='Sexo', choices=[(b'M', 'Masculino'), (b'F', 'Feminino')])),
                ('birthday', models.DateField(help_text='Insira sua data de nascimento.', null=True, verbose_name='Data de nascimento', blank=True)),
                ('credit', models.DecimalField(default=0, verbose_name='Saldo', max_digits=9, decimal_places=2)),
                ('city', models.ForeignKey(blank=True, to='account.City', null=True)),
                ('inviter', models.ForeignKey(blank=True, to='account.OferClubUser', null=True)),
            ],
            options={
                'verbose_name': 'Usu\xe1rio',
                'verbose_name_plural': 'Usu\xe1rios',
            },
            bases=('account.oferclubabstractuser',),
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(unique=True, max_length=255, db_index=True)),
                ('logo', models.ImageField(upload_to=b'parceiro/', null=True, verbose_name='Logomarca', blank=True)),
                ('slug', models.SlugField(unique=True, max_length=255, editable=False, blank=True)),
                ('cnpj', models.CharField(max_length=18, verbose_name='CNPJ')),
                ('phone', models.CharField(max_length=20, null=True, verbose_name='Telefone', blank=True)),
                ('cellphone', models.CharField(max_length=20, null=True, verbose_name='Celular', blank=True)),
                ('about', tinymce.models.HTMLField()),
            ],
            options={
                'verbose_name': 'Parceiro',
                'verbose_name_plural': 'Parceiros',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('acronym', models.CharField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='invite',
            name='invited_user',
            field=models.ForeignKey(related_name=b'invited', blank=True, to='account.OferClubUser', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invite',
            name='user',
            field=models.ForeignKey(to='account.OferClubUser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='filial',
            name='partner',
            field=models.ForeignKey(to='account.Partner'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(to='account.State'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='affiliate',
            name='city',
            field=models.ForeignKey(blank=True, to='account.City', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(to='account.City'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.ForeignKey(related_name=b'accounts', verbose_name='usu\xe1rio do OferClub', to='account.OferClubUser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='oferclubabstractuser',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='oferclubabstractuser',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
            preserve_default=True,
        ),
    ]
