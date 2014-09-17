# coding: utf-8
from collections import OrderedDict

from django import forms
from django.contrib.auth import authenticate
# from django.contrib.auth.hashers import UNUSABLE_PASSWORD
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.models import get_current_site
from django.template import loader
from django.utils.http import int_to_base36
from django.utils.translation import ugettext_lazy as _

from .models import OferClubUser

class EmailAuthenticationForm(forms.Form):
    """
    Form for authenticating users by their email address.
    """
    email = forms.EmailField(
        label=_(u'email'),
        max_length=254,
        widget=forms.TextInput(
            attrs={'class': 'form-control validaTxt',
                   'placeholder': 'EMAIL',
                   'autofocus': '', }),
        help_text=_(u'digite seu email.'))
    password = forms.CharField(
        label=_(u'password'),
        widget=forms.PasswordInput(
            attrs={'class': 'form-control validaTxt',
                   'placeholder': 'SENHA', }),
        help_text=_(u'digite sua senha.'))

    error_messages = {
        'invalid_login': _(u"Login e / ou senha incorretos."),
        'no_cookies': _(u"Seu navegador não possui cookies habilitados. "
                        u"Cookies são necessários para efeturar o login."),
        'inactive': _(u"Esta conta está inativa."),
    }

    def __init__(self, request=None, *args, **kwargs):
        """
        If request is passed in, the form will validate that cookies are
        enabled. Note that the request (a HttpRequest object) must have set a
        cookie with the key TEST_COOKIE_NAME and value TEST_COOKIE_VALUE before
        running this validation.
        """
        self.request = request
        self.user_cache = None
        super(EmailAuthenticationForm, self).__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(email=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'])
            elif not self.user_cache.is_active:
                raise forms.ValidationError(self.error_messages['inactive'])
        self.check_for_test_cookie()
        return self.cleaned_data

    def check_for_test_cookie(self):
        if self.request and not self.request.session.test_cookie_worked():
            raise forms.ValidationError(self.error_messages['no_cookies'])

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache