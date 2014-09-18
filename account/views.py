#coding: utf-8

import urlparse
from datetime import timedelta
from datetime import datetime
from urlparse import parse_qs
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
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy

from .models import OferClubUser, Account, get_facebook_service

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

def facebook_new(request):
    # get session
    facebook = get_facebook_service()

    # redirect to dialog
    params = {
        'redirect_uri': settings.FACEBOOK_CALLBACK_URL,
        'scope': [
            'email',
            'user_birthday',
        ],
    }
    authorization_url = facebook.get_authorize_url(**params)
    return redirect(authorization_url)


def facebook_callback(request):
    # get/check params
    redirect_uri = settings.FACEBOOK_CALLBACK_URL
    code = request.GET.get('code', None)
    if not code:
        return redirect('home')

    # get session
    facebook = get_facebook_service()

    # fetch tokens
    data = {
        'code': code,
        'redirect_uri': redirect_uri
    }

    r = facebook.get_raw_access_token(data=data)

    credentials = parse_qs(r.content)
    access_token = credentials.get('access_token')[0]
    expires = credentials.get('expires')[0]

    # get information about user
    client = facebook.get_session(token=access_token)

    me = client.get('me').json()

    # get or create a new user
    try:
        user = OferClubUser.objects.get(email=me['email'])
        gotosignup = False
    except OferClubUser.DoesNotExist:

        if me['gender'] == 'male':
            gender = 'M'
        elif me['gender'] == 'female':
            gender = 'F'

        birthday = datetime.strptime(me['birthday'], "%m/%d/%Y")

        user = OferClubUser.objects.create_user(
            email=me['email'],
            full_name=me['name'],
            gender=gender,
            birthday=birthday,
            password=OferClubUser.objects.make_random_password()
        )

        gotosignup = True
    # get or create new social account
    try:
        account = Account.objects.get(
            user=user,
            provider='facebook')
    except Account.DoesNotExist:
        account = Account.objects.create(
            user=user,
            provider='facebook',
            provider_id=me['id'],
            provider_username=me['id']
        )

        account.expires_in = datetime.now() + timedelta(seconds=int(expires))
        account.oauth_token = access_token
        account.save()
    # import pdb;pdb.set_trace()
    user = authenticate(email=user.email, oauth_token=account.oauth_token)
    auth_login(request, user)
    
    if gotosignup:
        # go to signup
        return signup_or_login(request, signup=True, json=me)
    else:
        # login successfully.
        return signup_or_login(request, signup=False, user=user, oauth_token=account.oauth_token)


def signup_or_login(request, signup=True, account=None, json=None, user=None, oauth_token=None):
    if signup:
        # facebook_user = account.get_client()
        # facebook_user_data = facebook_user.get('me').json()
        # or
        facebook_user_data = json
        if 'facebook_user_data' in request.session:
            del request.session['facebook_user_data']
        request.session['facebook_user_data'] = facebook_user_data

        return HttpResponseRedirect(reverse_lazy('offer:home', kwargs={'slug': 'x934nsdkpass'}))
    else:
        return login_social(request, user=user, oauth_token=oauth_token)


@sensitive_post_parameters()
@csrf_protect
@never_cache
def login_social(request, user=None, oauth_token=None):
    
    error_messages = {
        'invalid_social_login': _(
            u"Problems with your oauth token or your email. enter a correct email and password. "),
        'no_cookies': _(u"Your Web browser doesn't appear to have cookies "
                        "enabled. Cookies are required for logging in."),
        'inactive': _(u"Esta conta está inativa."),
    }

    email = user.email
    token = oauth_token

    request.session.set_test_cookie()

    if email and token:
        user_cache = authenticate(email=email, oauth_token=token)
        if user_cache is None:
            raise forms.ValidationError(
                error_messages['invalid_social_login'])
        elif not user_cache.is_active:
            raise forms.ValidationError(error_messages['inactive'])
    if request and not request.session.test_cookie_worked():
        raise forms.ValidationError(error_messages['no_cookies'])

    try:
        auth_login(request, user_cache)
    except Exception, e:
        raise e

    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()

    request.session.set_expiry(0)

    url = reverse_lazy('offer:home', kwargs={})

    return HttpResponseRedirect(url)