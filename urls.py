from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oferclub.views.home', name='home'),
    url(r'^', include('offer.urls', namespace="offer", app_name="offer")),
    url(r'^', include('account.urls', namespace="account", app_name="account")),

    url(r'^admin/', include(admin.site.urls)),
)
