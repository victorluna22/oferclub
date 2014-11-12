#coding: utf-8
import json
from datetime import datetime
from django.http import HttpResponse
from django.db.models import Count
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, FormView
from django.views.generic.detail import DetailView
from checkout.models import Coupon, Order, Operation
from account.models import OferClubUser
from offer.models import Offer, Category, Type, SubCategory, PromotionCode, Interest
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


class OfferListView(ListView):
    model = Offer
    template_name = u"offer/offer_list.html"
    paginate_by = 9
    category = None

    def get(self, *args, **kwargs):
        # import pdb;pdb.set_trace()
        if self.request.is_ajax():
            page_size = self.get_paginate_by(True)
            if page_size:
                try:
                    paginator, page, queryset, is_paginated = self.paginate_queryset(self.get_queryset(), page_size)
                except:
                    queryset = []
            return HttpResponse(json.dumps(Offer.objects.prepare_dict(queryset)), content_type='application/json')
        return super(OfferListView, self).get(*args, **kwargs)

    def get_queryset(self):
        query = Offer.objects.select_related('city').all().order_by('-date_created')

        if self.request.GET.get("category"):
            id_type = self.request.session.get('typeoffer')
            id_city = self.request.session.get('city')

            if self.request.GET.get("category") == 'ultimas-ofertas':
                return Offer.objects.select_related('city').filter(subcategory__category__type__id=id_type, city__id=id_city).order_by('-date_created')

            if self.request.GET.get("category") == 'mais-vendidos':
                return Offer.objects.select_related('city').filter(subcategory__category__type__id=id_type, city__id=id_city).order_by('-bought')   

            category = get_object_or_404(Category, slug=self.request.GET.get("category"))
            self.category = category
            query = query.filter(subcategory__category=category)

        if self.request.GET.get("subcategory"):
            subcategories = []
            for sub in self.request.GET.get("subcategory").split(','):
                subcategory = get_object_or_404(SubCategory, slug=sub)
                subcategories.append(subcategory)
            query = query.filter(subcategory__in=subcategories)

        if self.request.GET.get("interesses"):
            interests = []
            for interest in self.request.GET.get("interesses").split(','):
                obj = get_object_or_404(Interest, slug=interest)
                interests.append(obj)
            query = query.filter(interests__in=interests).distinct()

        if self.request.GET.get("order"):
            order = self.request.GET.get("order")
            if order == 'menor-preco':
                query = query.order_by('-options__new_price')
            elif order == 'maior-preco':
                query = query.order_by('title')
            elif order == 'mais-recentes':
                query = query.order_by('title')

        return query
        # return Offer.objects.prepare_dict(query)

    def get_context_data(self, *args, **kwargs):
        context = super(OfferListView, self).get_context_data(*args, **kwargs)
        context['destaques'] = Offer.objects.select_related('city').filter(highlight=True, options__start_time__lte=datetime.today(), options__end_time__gte=datetime.today()).distinct()
        if self.category:
            context['category'] = self.category
            context['subcategories'] = SubCategory.objects.filter(category=self.category).annotate(total=Count('offer'))
            context['interests'] = Interest.objects.filter(category=self.category).annotate(total=Count('offer'))
        else:
            id_type = self.request.session.get('typeoffer')
            id_city = self.request.session.get('city')
            context['ultimas_count'] = Offer.objects.select_related('city').filter(subcategory__category__type__id=id_type, city__id=id_city).count()
            context['mais_vendidos_count'] = Offer.objects.select_related('city').filter(subcategory__category__type__id=id_type, city__id=id_city).count()
            context['categories'] = Category.objects.filter(type__id=id_type).annotate(total=Count('subcategories__offer'))
        return context

class OfferDetailView(DetailView):
    model = Offer

    def get_context_data(self, *args, **kwargs):
        context = super(OfferDetailView, self).get_context_data(*args, **kwargs)
        context['partner'] = self.object.partner
        context['first_option'] = self.object.first_option()
        context['other_options'] = self.object.other_options()
        context['related_offers'] = self.object.related_offers()
        # import pdb;pdb.set_trace()
        context['images'] = self.object.images.all()
        return context


def home(request):
    context = {}
    data = []
    # import pdb;pdb.set_trace()
    id_type = request.session.get('typeoffer')
    id_city = request.session.get('city')
    latests = Offer.objects.latest_offers(id_type, id_city)
    if latests:
        data.append({"titulo_bloco": "Ultimas Ofertas", "category": "ultimas-ofertas", "ofertas": latests})
    bestsellers = Offer.objects.bestsellers(id_type, id_city)
    if bestsellers:
        data.append({"titulo_bloco": "Mais Vendidos", "category": "mais-vendidos", "ofertas": bestsellers})
    for category in Category.objects.filter(type__id=id_type):
        offers = category.get_offers_available(id_city)
        if offers:
            data.append({"titulo_bloco": category.name.encode('utf-8'), "category": category.slug, "ofertas": Offer.objects.prepare_dict(offers)})
    # blocks = serializers.serialize("json", data)
    
    blocks = json.dumps(data)
    context['json'] = blocks
    context['destaques'] = Offer.objects.select_related('city').filter(highlight=True, options__start_time__lte=datetime.today(), options__end_time__gte=datetime.today()).distinct()
    context['blocos'] = data
    return render(request, 'offer/home.html', context)

def change_product_type(request, slug):
    # import pdb;pdb.set_trace()
    type_offer = get_object_or_404(Type, slug=slug)
    request.session['typeoffer'] = int(type_offer.id)
    # return home(request)
    redirect_to = reverse_lazy('offer:home')
    return HttpResponseRedirect(redirect_to)


def checks_code(request, code):
    # import pdb;pdb.set_trace()
    result = PromotionCode.objects.filter(code=code, start_time__lte=datetime.today(), end_time__gte=datetime.today())
    if result:
        return HttpResponse(json.dumps({'error': False, 'discount': float(result[0].discount)}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'error': True}), content_type='application/json')