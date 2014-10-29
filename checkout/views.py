#coding: utf-8
import json
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404, redirect
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from pagseguro import PagSeguro
from .models import Order, ORDER_AUTHORIZED
from .forms import OrderCreateForm
from offer.models import Option
from offer.views import LoginRequiredMixin
from correios_frete.client import Client
from correios_frete.package import Package
from correios_frete.constants import CAIXA_PACOTE, SEDEX, PAC
# Create your views here.

class OrderCreateViewView(LoginRequiredMixin, CreateView):
	model = Order
	template_name = 'checkout/order_create.html'
	form_class = OrderCreateForm

	def get_context_data(self, **kwargs):
		context = super(OrderCreateViewView, self).get_context_data(**kwargs)
		if self.kwargs.get('option_id', ''):
			option = get_object_or_404(Option, pk=self.kwargs.get('option_id'))
			context['option'] = option
			context['total'] = max(0, option.new_price - self.request.user.credit)
			# import pdb;pdb.set_trace()
		context['range_quantity'] = range(option.offer.max_by_user)
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
					self.object.total = max(0, self.object.option.new_price * self.object.quantity - self.request.user.credit)
					if self.object.total == 0:
						self.object.status = ORDER_AUTHORIZED
					self.object.save()
					if self.object.total > 0:
						return redirect(self.object.pay_pagseguro())
					return HttpResponseRedirect(self.get_success_url())
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


def calculate_shipping(request, cep):
	value = request.GET.get('ofertas')
	if value:
		ofertas = value.split(',')
		package = Package(formato=CAIXA_PACOTE)
		for oferta in ofertas:
			option_id = oferta.split(':')[0]
			qtd = oferta.split(':')[1]
			option = get_object_or_404(Option, id=option_id)
			if option.offer.delivery:
				client = Client(cep_origem='01310-200')
				for i in range(int(qtd)):
					package.add_item(
						weight = float(option.weight) if option.weight else 0,
						height = float(option.height) if option.height else 0,
						width  = float(option.width) if option.width else 0,
						length = float(option.length) if option.length else 0
					)
			else:
				return HttpResponse(json.dumps({'error': 1, 'data': 'Oferta não possui a opção de entrega'}), content_type='application/json')
		servicos = client.calc_preco_prazo(package, cep, PAC)
		# import pdb;pdb.set_trace()
		if servicos[0].erro == 0:
			return HttpResponse(json.dumps({'error': servicos[0].erro, 'data': servicos[0].valor}), content_type='application/json')
		else:
			return HttpResponse(json.dumps({'error': 1, 'data': servicos[0].msg_erro}), content_type='application/json')
	return HttpResponse(json.dumps({'error': 1, 'data': ''}), content_type='application/json')