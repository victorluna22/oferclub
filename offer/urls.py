from django.conf.urls import patterns, include, url
from offer.views import OfferListView, OfferDetailView
from account.views import MyCouponsListView, MyOrdersListView, MyOperationsListView, OferClubUserEditView
from checkout.views import OrderCreateViewView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', OfferListView.as_view(), name='home'),
    url(r'^oferta/(?P<slug>[\w_-]+)$', OfferDetailView.as_view(), name='offer_detail'),
    url(r'^oferta/(?P<option_id>\d+)/comprar/$', OrderCreateViewView.as_view(), name='buy_offer'),

	    url(r'^usuario/', include(patterns('',
	    	url(r'^meus-cupons/$', MyCouponsListView.as_view(), name='my_coupons'),
	    	url(r'^meus-creditos/$', MyOperationsListView.as_view(), name='my_operations'),
	    	url(r'^minhas-compras/$', MyOrdersListView.as_view(), name='my_orders'),
	    	url(r'^editar-dados/$', OferClubUserEditView.as_view(), name='change_user'),
	    ), namespace='user')),

)
