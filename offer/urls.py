from django.conf.urls import patterns, include, url
from offer.views import OfferDetailView
from account.views import MyCouponsListView, MyOrdersListView, MyOperationsListView, OferClubUserEditView, \
InviteCreateView, change_city
from checkout.views import OrderCreateViewView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'offer.views.home', name='home'),
    url(r'^oferta/(?P<slug>[\w_-]+)/$', OfferDetailView.as_view(), name='offer_detail'),
    url(r'^oferta/(?P<option_id>\d+)/comprar/$', OrderCreateViewView.as_view(), name='buy_offer'),

	    url(r'^usuario/', include(patterns('',
	    	url(r'^meus-cupons/$', MyCouponsListView.as_view(), name='my_coupons'),
	    	url(r'^meus-creditos/$', MyOperationsListView.as_view(), name='my_operations'),
	    	url(r'^minhas-compras/$', MyOrdersListView.as_view(), name='my_orders'),
	    	url(r'^editar-dados/$', OferClubUserEditView.as_view(), name='change_user'),
	    	url(r'^convidar/$', InviteCreateView.as_view(), name='invite'),
	    	url(r'^mudar-cidade/$', change_city, name='change_city'),
	    ), namespace='user')),

)
