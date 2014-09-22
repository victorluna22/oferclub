from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
# import xadmin
admin.autodiscover()
# xadmin.autodiscover()

# from xadmin.plugins import xversion
# xversion.register_models()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oferclub.views.home', name='home'),
    url(r'^', include('offer.urls', namespace="offer", app_name="offer")),
    url(r'^', include('account.urls', namespace="account", app_name="account")),

    (r'^tinymce/', include('tinymce.urls')),


    # url(r'^admin/', include(xadmin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns("",
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True }),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT, }),
        )
