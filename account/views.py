#coding: utf-8

import urlparse
import json
import re
from datetime import timedelta
from datetime import datetime
from urlparse import parse_qs
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.views.generic.edit import FormView, UpdateView, CreateView
from django.views.generic.list import ListView
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
from django.contrib.auth.forms import SetPasswordForm
from django.template.response import TemplateResponse
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import base36_to_int
from django.shortcuts import get_object_or_404

from account.forms import EmailAuthenticationForm, OferClubAddressForm
from offer.views import LoginRequiredMixin
from offer.models import Option, Offer
from checkout.models import Coupon, Operation, Order, OrderItem
from .models import OferClubUser, Account, Invite, City, NewsLetter, Address, get_facebook_service
from .forms import OferClubUserForm, OferClubUserChangeForm, InviteCreateForm, NewsLetterForm


class MyCouponsListView(LoginRequiredMixin, ListView):
    model = Coupon
    template_name = u"account/user/coupons.html"

    def get_queryset(self):
        user = self.request.user
        return Coupon.objects.select_related('order_item__option').filter(order_item__order__user=user)

    def get_context_data(self, *args, **kwargs):
        context =  super(MyCouponsListView, self).get_context_data(*args, **kwargs)
        context['destaques'] = Offer.objects.select_related('city').filter(highlight=True, options__start_time__lte=datetime.today(), options__end_time__gte=datetime.today()).distinct()
        return context

class MyOrdersListView(LoginRequiredMixin, ListView):
    model = Coupon
    template_name = u"account/user/orders.html"

    def get_queryset(self):
        user = self.request.user
        return OrderItem.objects.select_related('option').filter(order__user=user)

class MyOperationsListView(LoginRequiredMixin, ListView):
    model = Operation
    template_name = u"account/user/operations.html"

    def get_queryset(self):
        user = self.request.user
        return Operation.objects.filter(user=user)

class OferClubUserEditView(LoginRequiredMixin, UpdateView):
    model = OferClubUser
    form_class = OferClubUserChangeForm
    template_name = 'account/user/edit_user.html'
    success_url = reverse_lazy('offer:user:change_user')

    def get_object(self):
        return self.request.user

    def form_invalid(self, form):
        # import pdb;pdb.set_trace()
        return super(OferClubUserEditView, self).form_invalid(form)


class OferClubAddressEditView(LoginRequiredMixin, UpdateView):
    model = Address
    form_class = OferClubAddressForm
    template_name = 'account/user/edit_address.html'
    success_url = reverse_lazy('offer:user:change_user_address')

    def get_object(self):
        try:
            return self.request.user.address.all()[0]
        except:
            return None

class OferClubCreateView(FormView):
    form_class = OferClubUserForm
    context_object_name = 'object'
    template_name = 'account/login.html'
    success_url = reverse_lazy('offer:home')

    def form_valid(self, form):
        full_name = form.cleaned_data['full_name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        city = form.cleaned_data['city']
        gender = form.cleaned_data['gender']
        birthday = form.cleaned_data['birthday']
        inviter = None
        if self.request.session.get('invite'):
            invite = Invite.objects.get_invite_by_code(self.request.session.get('invite'))
            if invite and invite.email == email:
                inviter = invite.user
        OferClubUser.objects.create_user(email=email, password=password, full_name=full_name, city=city, gender=gender, birthday=birthday, inviter=inviter)
        user = authenticate(email=email, password=password)
        auth_login(self.request, user)
        return super(OferClubCreateView, self).form_valid(form)

    def get_initial(self):
        # import pdb;pdb.set_trace()
        if self.request.GET.get('token'):
            self.request.session['invite'] = self.request.GET.get('token')
        if self.request.session.get('invite'):
            invite = Invite.objects.get_invite_by_code(self.request.session['invite'])
            if invite:
                return {'email': invite.email}


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

    def form_invalid(self, form):
        return super(LoginView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context.update({
            'redirect_to': self.redirect_to,
            'redirect_field_name': self.redirect_field_name,
        })
        if self.request.GET.get('next'):
            result = re.match(r'^/oferta/(?P<id>\d+)/comprar/$', self.request.GET.get('next'))
            if result:
                id = result.groupdict()['id']
                try:
                    context['option'] = Option.objects.select_related('offer').get(id=id)
                except:
                    pass
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


@sensitive_post_parameters()
@never_cache
def password_reset_confirm(request, uidb36=None, token=None,
                           template_name='registration/password_reset_confirm.html',
                           token_generator=default_token_generator,
                           set_password_form=SetPasswordForm,
                           post_reset_redirect=None,
                           current_app=None, extra_context=None):
    """
    View that checks the hash in a password reset link and presents a
    form for entering a new password.
    """
    assert uidb36 is not None and token is not None  # checked by URLconf
    if post_reset_redirect is None:
        post_reset_redirect = reverse('django.contrib.auth.views.password_reset_complete')
    try:
        uid_int = base36_to_int(uidb36)
        user = OferClubUser.objects.get(pk=uid_int)
    except (ValueError, OverflowError, OferClubUser.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        validlink = True
        if request.method == 'POST':
            form = set_password_form(user, request.POST)
            if form.is_valid():
                new_user = form.save(commit=False)
                new_user.has_password = True
                new_user.save()
                return HttpResponseRedirect(post_reset_redirect)
        else:
            form = set_password_form(None)
    else:
        validlink = False
        form = None
    context = {
        'form': form,
        'validlink': validlink,
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)


class InviteCreateView(LoginRequiredMixin, CreateView):
    model = Invite
    template_name = 'account/user/invite.html'
    form_class = InviteCreateForm

    def form_valid(self, form):
        # import pdb;pdb.set_trace()
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        self.object.mail_invite()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        # import pdb;pdb.set_trace()
        for error in json.loads(form.errors.as_json())['email']:
            if error['code'] == 'already_exists':
                return super(InviteCreateView, self).form_invalid(form)
            if error['code'] == 'unique':
                invite = Invite.objects.get(email=form.data['email'])
                if invite:
                    invite.invite_date = datetime.now()
                    invite.user = self.request.user
                    invite.save()
                    invite.mail_invite()
                    return HttpResponseRedirect(self.get_success_url())
        return super(InviteCreateView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('offer:user:invite', kwargs={})



def change_city(request):
    # import pdb;pdb.set_trace()
    if request.POST and request.POST.get('city'):
        city_id = request.POST.get('city')
        city = get_object_or_404(City, pk=city_id)
        request.session['city'] = city.id
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class NewsLetterCreateView(FormView):
    model = NewsLetter
    # template_name = 'account/user/invite.html'
    form_class = NewsLetterForm

    def get_success_url(self):
        return reverse_lazy('offer:home', kwargs={})

    def form_valid(self, form):
        city_id = self.request.session['city']
        city = get_object_or_404(City, pk=city_id)
        newsletter = form.save(commit=False)
        newsletter.city = city
        newsletter.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form): 
        return HttpResponseRedirect(self.get_success_url())