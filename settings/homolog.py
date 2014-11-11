from .base import *

DEBUG = True

TEMPLATE_DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'oferclub',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}

INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
)

STATIC_URL = '/static/'

STATIC_ROOT = '/home/ubuntu/statics/oferclub/static'

MEDIA_URL = '/media/'

MEDIA_ROOT = '/var/www/statics/oferclub/media'

INTERNAL_IPS = ['54.172.25.31',]
