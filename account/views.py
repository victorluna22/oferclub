#coding: utf-8

import urlparse
from django.shortcuts import render
from account.forms import EmailAuthenticationForm
from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.views.generic.edit import FormView
from django.views.decorators.cache import never_cache
from django.contrib.sites.models import Site
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

# Create your views here.


class LoginView(FormView):
    template_name = 'account/login.html'
    redirect_field_name = REDIRECT_FIELD_NAME
    form_class = EmailAuthenticationForm

    #TODO if is staff redirect to admin (or ask where want to go)
    #TODO redirect already authenticated user to his wedding panel
    # @redirect_authenticated_user(redirect_field_name=REDIRECT_FIELD_NAME, redirect_url=settings.LOGIN_REDIRECT_URL)
    @never_cache
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(settings.LOGIN_REDIRECT_URL)
        self.redirect_to = request.GET.get(self.redirect_field_name, '')
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        redirect_to = self.redirect_to
        netloc = urlparse.urlparse(redirect_to)[1]

        # Use default setting if redirect_to is empty
        if not redirect_to:
            redirect_to = settings.LOGIN_REDIRECT_URL

        # Heavier security check -- don't allow redirection to a different host.
        elif netloc and netloc != self.request.get_host():
            redirect_to = settings.LOGIN_REDIRECT_URL

        # Okay, security checks complete. Log the user in.
        auth_login(self.request, form.get_user())

        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        if self.request.POST.get('remember_me', None):
            self.request.session.set_expiry(settings.KEEP_LOGGED_DURATION)
        else:
            self.request.session.set_expiry(0)

        # if not form.get_user().wedding:
        #     redirect_to = reverse_lazy('wedding:create')

        return HttpResponseRedirect(redirect_to)

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context.update({
            'redirect_to': self.redirect_to,
            'redirect_field_name': self.redirect_field_name,
            # 'site': Site.objects.get_current(),
        })
        return context