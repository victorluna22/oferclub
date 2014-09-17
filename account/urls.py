from django.conf.urls import patterns, include, url
from django.contrib.auth.views import logout
from django.core.urlresolvers import reverse_lazy
from account.views import LoginView
from account.forms import EmailAuthenticationForm

urlpatterns = patterns('',
    # Examples:
    url(r'^login/$', LoginView.as_view(),
        {'template_name': 'account/login.html',
         'authentication_form': EmailAuthenticationForm},
        name='login'),

    # django logout
    url(r'^logout/$', logout,
        {'next_page': reverse_lazy('login')},
        name='logout'),

)
