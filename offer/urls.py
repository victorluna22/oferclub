from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from offer.views import OfferDetailView, OfferListView, OfferSearchListView
from account.views import MyCouponsListView, MyOrdersListView, MyOperationsListView, OferClubUserEditView, \
InviteCreateView, OferClubAddressEditView, change_city
from checkout.views import OrderCreateViewView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'offer.views.home', name='home'),
    url(r'^email/$', 'offer.views.email', name='email'),
    url(r'^selecionar/(?P<slug>[\w_-]+)/$', 'offer.views.change_product_type', name='change_product_type'),
    url(r'^oferta/listagem/$', OfferListView.as_view(), name='offer_list'),
    url(r'^oferta/pesquisa/$', OfferSearchListView.as_view(), name='search'),
    url(r'^oferta/(?P<slug>[\w_-]+)/$', OfferDetailView.as_view(), name='offer_detail'),
    url(r'^oferta/(?P<option_id>\d+)/comprar/$', 'checkout.views.order_create_view', name='buy_offer'),
    url(r'^verifica-codigo/(?P<code>[\w_-]+)/$', 'offer.views.checks_code', name='checks_code'),
    url(r'^calcular-frete/(?P<cep>[\w_-]+)/$', 'checkout.views.calculate_shipping_view', name='calculate_shipping'),

	    url(r'^usuario/', include(patterns('',
	    	url(r'^meus-cupons/$', MyCouponsListView.as_view(), name='my_coupons'),
	    	url(r'^meus-creditos/$', MyOperationsListView.as_view(), name='my_operations'),
	    	url(r'^minhas-compras/$', MyOrdersListView.as_view(), name='my_orders'),
	    	url(r'^dados-pessoais/conta/$', OferClubUserEditView.as_view(), name='change_user'),
	    	url(r'^dados-pessoais/endereco/$', OferClubAddressEditView.as_view(), name='change_user_address'),
	    	url(r'^convidar/$', InviteCreateView.as_view(), name='invite'),
	    	url(r'^mudar-cidade/$', change_city, name='change_city'),
	    ), namespace='user')),


	# Static Pages
	url(r'^atendimento/$', TemplateView.as_view(template_name='institucional/customer_service.html'), name="customer_service"),
	url(r'^sobre-nos/$', TemplateView.as_view(template_name='institucional/about_us.html'), name="about_us"),
	url(r'^termo-de-uso/$', TemplateView.as_view(template_name='institucional/use_terms.html'), name="use_terms"),
	url(r'^como-funciona/$', TemplateView.as_view(template_name='institucional/how_to_work.html'), name="how_to_work"),
	url(r'^seja-parceiro/$', TemplateView.as_view(template_name='institucional/be_partner.html'), name="be_partner"),
	url(r'^nosso-parceiro/$', TemplateView.as_view(template_name='institucional/our_partner.html'), name="our_partner"),
	url(r'^dinheiro-de-volta/$', TemplateView.as_view(template_name='institucional/cashback.html'), name="cashback"),
	url(r'^receba-ofertas/$', TemplateView.as_view(template_name='institucional/receive_offers.html'), name="receive_offers"),
	url(r'^fale-conosco/$', TemplateView.as_view(template_name='institucional/contact_us.html'), name="contact_us"),
	url(r'^perguntas-frequentes/$', TemplateView.as_view(template_name='institucional/faq.html'), name="faq"),
	url(r'^politica-de-compra/$', TemplateView.as_view(template_name='institucional/buy_policy.html'), name="buy_policy"),

)
