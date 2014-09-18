from django.conf.urls import patterns, include, url
from django.contrib.auth.views import logout
from django.core.urlresolvers import reverse_lazy
from account.views import LoginView, facebook_new, facebook_callback
from account.forms import EmailAuthenticationForm

urlpatterns = patterns('',

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

)
