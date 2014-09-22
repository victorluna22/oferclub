from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from .models import Order
from offer.models import Option
from offer.views import LoginRequiredMixin
# Create your views here.

class OrderCreateViewView(LoginRequiredMixin, CreateView):
    model = Order
    template_name = 'checkout/order_create.html'
    fields = ('quantity',)

    def get_context_data(self, **kwargs):
        context = super(OrderCreateViewView, self).get_context_data(**kwargs)
        if self.kwargs.get('option_id', ''):
        	context['option'] = get_object_or_404(Option, pk=self.kwargs.get('option_id'))
        return context