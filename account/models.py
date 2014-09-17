# -*- coding: utf-8 -*-

from datetime import timedelta
from datetime import datetime
import re

from rauth import OAuth2Service

from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from account.slugify import unique_slugify as slugify


try:
    from django.utils.timezone import now as datetime_now
except ImportError:
    datetime_now = datetime.now

SHA1_RE = re.compile('^[a-f0-9]{40}$')
FACEBOOK_APP_ID = settings.FACEBOOK_APP_ID
FACEBOOK_APP_SECRET = settings.FACEBOOK_APP_SECRET
FACEBOOK_CALLBACK_URL = settings.FACEBOOK_CALLBACK_URL

GENDER_CHOICES = (('M', _(u'Masculino')),
                  ('F', _(u'Feminino')),)

PROVIDER_CHOICES = (
    (u'facebook', u'Facebook'),
)


def get_facebook_service():
    facebook = OAuth2Service(
        client_id=FACEBOOK_APP_ID,
        client_secret=FACEBOOK_APP_SECRET,
        name='facebook',
        authorize_url='https://www.facebook.com/dialog/oauth',
        access_token_url='https://graph.facebook.com/oauth/access_token',
        base_url='https://graph.facebook.com/'
    )
    return facebook



class OferClubUserManager(BaseUserManager):
    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()

        if email:
            # raise ValueError(_(u'É necessário um email válido.'))
            email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


class OferClubAbstractUser(AbstractBaseUser, PermissionsMixin):
    """
    A fully featured User model with admin-compliant permissions that uses
    a full-length email field as the username.

    Email and password are required. Other fields are optional.
    """
    # TODO: make full_name obligatory
    full_name = models.CharField(verbose_name=_(u'Nome completo'), max_length=200)
    email = models.EmailField(verbose_name=_(u'Email'), max_length=254, unique=True, db_index=True, null=True, blank=True)
    is_staff = models.BooleanField(verbose_name=_(u'Membro da equipe'), default=False,
                                   help_text=_(u'Designa se este usuário pode acessar este site admin.'))
    is_active = models.BooleanField(verbose_name=_(u'Ativo'), default=True,
                                    help_text=_(u'Designa se este usuário está ativo.'
                                                u'Desmarque esta opção ao invés de deletar a conta.'))
    date_joined = models.DateTimeField(verbose_name=_(u'Criado em'), default=timezone.now)
    slug = models.SlugField(max_length=255, blank=True, unique=True, editable=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    class Meta:
        verbose_name = _(u'usuário do Lua de Véu')
        verbose_name_plural = _(u'usuários do Lua de Véu')

    def save(self, *args, **kwargs):
        self.slug = slugify(instance=self,
                            value=self.full_name,
                            slug_separator=settings.SLUGFIELD_SEPARATOR)
        super(OferClubAbstractUser, self).save(*args, **kwargs)

    objects = OferClubUserManager()

    def __unicode__(self):
        return u'%s (%s)' % (self.get_full_name(), self.email)


    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        return self.full_name.strip().title() if self.full_name else self.email

    def get_short_name(self):
        """
        Returns the short name for the user.
        """

        return self.full_name.split()[0] if self.full_name else self.email


    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, 'contato@ofer.club', [self.email])


class State(models.Model):
    name = models.CharField(max_length=100)
    acronym = models.CharField(max_length=2)

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State)


class Address(models.Model):
    cep = models.CharField(max_length=9)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=100)
    complement = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    city = models.ForeignKey(City)


class OferClubUser(OferClubAbstractUser):
    city = models.ForeignKey(City, blank=True, null=True)
    gender = models.CharField(verbose_name=_(u'Sexo'), max_length=1, blank=True, null=True, choices=GENDER_CHOICES)
    birthday = models.DateField(verbose_name=_(u'Data de nascimento'), blank=True, null=True,
                                help_text=_(u'Insira sua data de nascimento.'))
    credit = models.DecimalField(verbose_name=_(u'Saldo'), max_digits=9, decimal_places=2, default=0)
    objects = OferClubUserManager()

    class Meta:
        verbose_name = _(u'Usuário')
        verbose_name_plural = _(u'Usuários')


class Partner(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    slug = models.SlugField(max_length=255, blank=True, unique=True, editable=False)
    cnpj = models.CharField(verbose_name=_(u'CNPJ'), max_length=18)
    phone = models.CharField(verbose_name=_(u'Telefone'), max_length=20)
    cellphone = models.CharField(verbose_name=_(u'Celular'), max_length=20)

    def save(self, *args, **kwargs):
        self.slug = slugify(instance=self,
                            value=self.name,
                            slug_separator=settings.SLUGFIELD_SEPARATOR)
        super(Partner, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.email)

    class Meta:
        verbose_name = _(u'Parceiro')
        verbose_name_plural = _(u'Parceiros')


class Filial(OferClubAbstractUser):
    partner = models.ForeignKey(Partner)
    city = models.ForeignKey(City, blank=True, null=True)
    phone = models.CharField(verbose_name=_(u'Telefone'), max_length=20)
    cellphone = models.CharField(verbose_name=_(u'Celular'), max_length=20)

    owner_name = models.CharField(
        verbose_name=_(u'Nome do Titular'),
        max_length=200,
        blank=True,
        null=True,
        help_text=_(u'Nome do titular'))
    bank_name = models.CharField(
        verbose_name=_(u'Banco'),
        max_length=100,
        blank=True,
        null=True,
        help_text=_(u'Nome do banco'))
    agency = models.CharField(
        verbose_name=_(u'Agência'),
        max_length=100,
        blank=True,
        null=True,
        help_text=_(u'Código da agência'))
    number = models.CharField(
        verbose_name=_(u'Conta'),
        max_length=100,
        blank=True,
        null=True,
        help_text=_(u'Número da conta'))
    cpf = models.CharField(
        verbose_name=_('CPF'),
        max_length=14,
        blank=True,
        null=True,
        help_text=_(u'CPF do proprietário da conta'))
    

    class Meta:
        verbose_name = _(u'Filial')
        verbose_name_plural = _(u'Filiais')


    def __unicode__(self):
        return u'%s (%s)' % (self.full_name, self.email)


class Affiliate(OferClubAbstractUser):
    city = models.ForeignKey(City, blank=True, null=True)
    phone = models.CharField(verbose_name=_(u'Telefone'), max_length=20)
    cellphone = models.CharField(verbose_name=_(u'Celular'), max_length=20)

    owner_name = models.CharField(
        verbose_name=_(u'Nome do Titular'),
        max_length=200,
        blank=True,
        null=True,
        help_text=_(u'Nome do titular'))
    bank_name = models.CharField(
        verbose_name=_(u'Banco'),
        max_length=100,
        blank=True,
        null=True,
        help_text=_(u'Nome do banco'))
    agency = models.CharField(
        verbose_name=_(u'Agência'),
        max_length=100,
        blank=True,
        null=True,
        help_text=_(u'Código da agência'))
    number = models.CharField(
        verbose_name=_(u'Conta'),
        max_length=100,
        blank=True,
        null=True,
        help_text=_(u'Número da conta'))
    cpf = models.CharField(
        verbose_name=_('CPF'),
        max_length=14,
        blank=True,
        null=True,
        help_text=_(u'CPF do proprietário da conta'))
    

    class Meta:
        verbose_name = _(u'Afiliado')
        verbose_name_plural = _(u'Afiliados')


    def __unicode__(self):
        return u'%s (%s)' % (self.full_name, self.email)


class Account(models.Model):
    user = models.ForeignKey(
        OferClubUser,
        verbose_name=_(u'usuário do OferClub'),
        related_name='accounts'
    )

    provider = models.CharField(
        _(u'provedor'),
        max_length=20,
        db_index=True,
        choices=PROVIDER_CHOICES
    )

    provider_id = models.CharField(
        _(u'id no provedor'),
        max_length=100
    )

    provider_username = models.CharField(
        _(u'login no provedor'),
        max_length=100
    )

    oauth_token = models.CharField(
        _(u'oauth token'),
        max_length=254
    )

    oauth_token_secret = models.CharField(
        _(u'oauth token secret'),
        max_length=254
    )

    refresh_token = models.CharField(
        _(u'refresh token'),
        max_length=254
    )

    expires_in = models.DateTimeField(
        _(u'expira em'),
        null=True
    )

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return _(u'provedor: {0} - login: {1}').format(
            self.provider, self.provider_username
        )

    class Meta:
        verbose_name = u'conta'
        verbose_name_plural = u'contas'

    def is_expired(self):
        if self.expires_in:
            return datetime.now() > self.expires_in - timedelta(minutes=10)
        return False

    def get_client(self):
        client = None

        if self.provider == 'facebook':
            client = get_facebook_service().get_session(
                token=self.oauth_token
            )

        return client


