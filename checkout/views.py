#coding: utf-8
import json
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404, redirect
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.db import transaction
from pagseguro import PagSeguro
from .models import Order, OrderItem, ORDER_AUTHORIZED
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
			context['other_options'] = option.offer.options.all()
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

@transaction.commit_on_success
def order_create_view(request, option_id):
	option = get_object_or_404(Option, pk=option_id)

	if request.POST:
		name_consumer = request.POST.get('name_consumer[]')
		option_id = request.POST.get('option_id[]')
		quantity = request.POST.get('quantity[]')
		order_total = 0
		offers_shipping = ""

		#SUBTOTAIS
		if len(name_consumer) == len(option_id) and len(option_id) == len(quantity):
			order = Order.objects.create(user=request.user, status=2, total=0)
			for i in range(len(name_consumer)):
				opt = get_object_or_404(Option, pk=option_id[i])
				item_total = int(quantity) * option.new_price
				order_item = OrderItem.objects.create(order=order, name_consumer=name_consumer[i], option=opt, quantity=quantity[i], total=item_total)
				order_total += item_total
				offers_shipping += ",%s:%s" % (opt.id, quantity[i])

		#FRETE
		if option.offer.delivery and request.POST.get('cep'):
			result = calculate_shipping(request.POST.get('cep'), offers_shipping[1:])
			if result['error'] != 0:
				return HttpResponse('erro frete: %s' % result['data'])
			else:
				order_total += float(result['data'])

		#CUPOM DE DESCONTO
		if request.POST.get('code_discount'):
			result = PromotionCode.objects.filter(code=request.POST.get('code_discount'), start_time__lte=datetime.today(), end_time__gte=datetime.today())
			if result:
				order_total -= result[0].discount

		# SALDO DE COMPRA
		if request.POST.get('use_credit', False):
			if request.user.credit <= order_total:
				order_total -= request.user.credit
			else:
				request.user.credit -= order_total
				request.user.save()
				order_total = 0



	context = {}
	context['option'] = option
	context['other_options'] = option.offer.options.all()
	context['range_quantity'] = range(option.offer.max_by_user)
	return render(request, 'checkout/order_create.html', context)


def calculate_shipping_view(request, cep):
	value = request.GET.get('ofertas')
	if value:
		result = calculate_shipping(cep, value)
		return HttpResponse(json.dumps(result), content_type='application/json')
	return HttpResponse(json.dumps({'error': 1, 'data': ''}), content_type='application/json')

def calculate_shipping(cep, offers):
	offers = offers.split(',')
	package = Package(formato=CAIXA_PACOTE)
	for offer in offers:
		option_id = offer.split(':')[0]
		qtd = offer.split(':')[1]
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
			return {'error': 1, 'data': 'Oferta não possui a opção de entrega'}
	services = client.calc_preco_prazo(package, cep, PAC)
	if services[0].erro == 0:
		return {'error': services[0].erro, 'data': services[0].valor}
	else:
		return {'error': 1, 'data': services[0].msg_erro}