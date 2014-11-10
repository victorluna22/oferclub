# coding: utf-8
from collections import OrderedDict

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.models import get_current_site
from django.template import loader
from django.utils.http import int_to_base36
from django.utils.translation import ugettext_lazy as _

from .models import OferClubUser, Invite, NewsLetter, Address


class OferClubUserForm(forms.ModelForm):
    error_messages = {
        'duplicate_email': _(u'Este email já está em uso. Por favor forneça um endereço de email diferente.'),
        'password_mismatch': _(u'As duas senhas digitadas não conferem.'),
    }

    full_name = forms.CharField(
        label=_(u'Nome Completo'),
        max_length=254,
        widget=forms.TextInput(
            attrs={'class': 'form-control validaTxt',
                   'placeholder': _(u'NOME COMPLETO') }),
        help_text=_(u'digite seu nome.'))

    birthday = forms.DateField(
        label=_(u'Data de aniversário'),
        required=False,
        input_formats=['%d-%m-%Y', '%d/%m/%Y'],
        widget=forms.DateInput(
            attrs={'class': 'form-control validaTxt',
                   'placeholder': _(u'DATA DE ANIVERSÁRIO') },
                   format='%d/%m/%Y'))

    email = forms.EmailField(
        label=_(u'email'),
        max_length=254,
        widget=forms.TextInput(
            attrs={'class': 'form-control validaTxt email',
                   'placeholder': _(u'EMAIL'),
                   'autofocus': '', }),
        help_text=_(u'digite seu email.'))

    password = forms.CharField(
        label=_(u'password'),
        widget=forms.PasswordInput(
            attrs={'class': 'form-control validaTxt password',
                   'placeholder': _(u'SENHA'), }),
        help_text=_(u'digite sua senha.'))

    confirm_password = forms.CharField(
        label=u'Confirmar senha',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control validaTxt password',
                   'placeholder': _(u'CONFIRMAR SENHA'), }),
        help_text=_(u'confirme sua senha.'))

    class Meta:
        model = OferClubUser
        fields = ('email', 'password', 'gender', 'birthday', 'city', 'full_name')
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def clean_email(self):
        if OferClubUser.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(self.error_messages['duplicate_email'])
        return self.cleaned_data['email']

    def clean_confirm_password(self):
        password1 = self.cleaned_data.get('password', '')
        password2 = self.cleaned_data['confirm_password']
        if password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'])
        return password2

    def save(self, commit=True):
        user = super(OferClubUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class OferClubAddressForm(forms.ModelForm):
    class Meta:
        model = Address

class OferClubUserChangeForm(forms.ModelForm):
    class Meta:
        model = OferClubUser
        fields = ('full_name', 'gender', 'birthday', 'avatar')


class PasswordResetForm(forms.Form):
    email = forms.EmailField(label=_(u'email'), max_length=254,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    def save(self, domain_override=None,
             subject_template_name='account/password_reset_subject.txt',
             email_template_name='account/password_reset_email.html',
             use_https=False, token_generator=default_token_generator,
             from_email=None, request=None, html_email_template_name=None):
        """
        Generates a one-use only link for resetting password and sends to the
        user.
        """
        from django.core.mail import send_mail

        email = self.cleaned_data['email']
        users = OferClubUser.objects.filter(email__iexact=email)
        for user in users:
            # Make sure that no email is sent to a user that actually has
            # a password marked as unusable
            if not user.has_usable_password():
                continue
            if not domain_override:
                current_site = get_current_site(request)
                site_name = current_site.name
                domain = current_site.domain
            else:
                site_name = domain = domain_override
            c = {
                'email': user.email,
                'domain': domain,
                'site_name': site_name,
                'uid': int_to_base36(user.pk),
                'user': user,
                'token': token_generator.make_token(user),
                'protocol': use_https and 'https' or 'http',
            }
            subject = loader.render_to_string(subject_template_name, c)
            # Email subject *must not* contain newlines
            subject = ''.join(subject.splitlines())
            email = loader.render_to_string(email_template_name, c)
            send_mail(subject, email, from_email, [user.email])


class SetPasswordForm(forms.Form):
    """
    A form that lets a user change set his/her password without entering the
    old password
    """
    error_messages = {
        'password_mismatch': _("As duas senhas digitadas não conferem."),
    }
    new_password1 = forms.CharField(label=_(u'nova senha'),
                                    widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label=_(u'nova senha (confirmação)'),
                                    widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SetPasswordForm, self).__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        return password2

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['new_password1'])
        if commit:
            self.user.save()
        return self.user



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


class InviteCreateForm(forms.ModelForm):
    class Meta:
        model = Invite
        fields = ('email',)

    def clean_email(self):
        if OferClubUser.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError('Já existe um usuário ativo com este E-mail!', code='already_exists')

        return self.cleaned_data['email']



class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ('email',)


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address