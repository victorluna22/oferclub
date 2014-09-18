from django.conf.urls import patterns, include, url
from django.contrib.auth.views import logout
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import password_reset
from django.contrib.auth.views import password_reset_complete
from django.contrib.auth.views import password_reset_done
from .forms import PasswordResetForm

from account.views import LoginView, OferClubCreateView, facebook_new, facebook_callback, password_reset_confirm
from account.forms import EmailAuthenticationForm, SetPasswordForm

urlpatterns = patterns('',
	url(r'^cadastrar/$', OferClubCreateView.as_view(),
        name='signup'),

	url(r'^new/facebook/$', facebook_new,
        name='accounts_facebook_new'),
    url(r'^new/facebook/callback/$', facebook_callback,
        name='accounts_facebook_callback'),


    url(r'^login/$', LoginView.as_view(),
        {'template_name': 'account/login.html',
         'authentication_form': EmailAuthenticationForm},
        name='login'),

    url(r'^logout/$', logout,
        {'next_page': reverse_lazy('account:login', kwargs={})},
        name='logout'),




    url(r'^senha/recuperar/$', password_reset,
        {'template_name': 'account/password_reset_form.html',
         'email_template_name': 'account/password_reset_email.html',
         'html_email_template_name': 'account/password_reset_email.html',
         'subject_template_name': 'account/password_reset_subject.txt',
         'post_reset_redirect': reverse_lazy('account:password_reset_done'),
         'from_email': settings.DEFAULT_FROM_EMAIL,
         'password_reset_form': PasswordResetForm},
        name='password_reset'),

    url(r'^senha/recuperar/realizado/$', password_reset_done,
        {'template_name': 'account/password_reset_done.html', },
        name='password_reset_done'),

    url(r'^senha/recuperar/confirmar/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm,
        {'template_name': 'accounts/password_reset_confirm.html',
         'post_reset_redirect': reverse_lazy('accounts:password_reset_complete'),
         'set_password_form': SetPasswordForm, },
        name='password_reset_confirm'),

)
