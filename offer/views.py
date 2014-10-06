#coding: utf-8
from django.core import serializers
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, FormView
from django.views.generic.detail import DetailView
from checkout.models import Coupon, Order, Operation
from account.models import OferClubUser
from offer.models import Offer, Category
from account.forms import OferClubUserForm, OferClubUserChangeForm

class LoginRequiredMixin(object):

    """
    View mixin which requires that the user is authenticated.
    Due to parent class order traversal this mixin must be
    added as the left most mixin of a view.
    """
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


# class OfferListView(ListView):
#     model = Offer
#     template_name = u"offer/home.html"

#     def get_queryset(self):
#         return Offer.objects.all()

class OfferDetailView(DetailView):
    model = Offer


def home(request):
    context = {}
    data = []
    data.append({"titulo_bloco": "Ultimas Ofertas", "ofertas": Offer.objects.latest_offers()})
    data.append({"titulo_bloco": "Mais Vendidos", "ofertas": Offer.objects.bestsellers()})
    for category in Category.objects.all():
        offers = Offer.objects.filter(category=category).order_by('-date_created')
        if offers:
            data.append({"titulo_bloco": str(category.name), "ofertas": Offer.objects.prepare_dict(offers)})
    # blocks = serializers.serialize("json", data)
    import json
    blocks = json.dumps(data)
    context['blocks'] = blocks
    return render(request, 'offer/home.html', context)

