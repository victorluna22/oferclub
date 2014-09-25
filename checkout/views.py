#coding: utf-8
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404, redirect
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from pagseguro import PagSeguro
from .models import Order
from .forms import OrderCreateForm
from offer.models import Option
from offer.views import LoginRequiredMixin
# Create your views here.

class OrderCreateViewView(LoginRequiredMixin, CreateView):
	model = Order
	template_name = 'checkout/order_create.html'
	form_class = OrderCreateForm

	def get_context_data(self, **kwargs):
		context = super(OrderCreateViewView, self).get_context_data(**kwargs)
		if self.kwargs.get('option_id', ''):
			context['option'] = get_object_or_404(Option, pk=self.kwargs.get('option_id'))
		return context

	def form_valid(self, form):
		# import pdb;pdb.set_trace()
		option = get_object_or_404(Option, pk=self.kwargs.get('option_id'))
		if option.is_available():
			if int(form.cleaned_data['quantity']) <= int(option.offer.max_by_user):
				if int(option.quantity) >= int(form.cleaned_data['quantity']):
					self.object = form.save(commit=False)
					self.object.user = self.request.user
					self.object.option = option
					self.object.total = self.object.option.new_price * self.object.quantity
					self.object.save()
					url = self.object.pay_pagseguro()
					return redirect(url)
				else:
					form.errors['quantity'] = 'Restam apenas %d cupons para esta oferta!' % int(option.quantity)
			else:
				form.errors['quantity'] = 'Você ultrapassou o limite máximo de cupons por usuário!'
		else:
			form.errors['quantity'] = 'Esta oferta não está mais disponível para compra!'
		return super(OrderCreateViewView, self).form_invalid(form)

	def form_invalid(self, form):
		# import pdb;pdb.set_trace()
		return super(OrderCreateViewView, self).form_invalid(form)

	def get_success_url(self):
		return reverse_lazy('offer:user:my_orders', kwargs={})