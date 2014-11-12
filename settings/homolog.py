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

STATIC_ROOT = '/var/www/statics/oferclub/static'

MEDIA_URL = '/media/'

MEDIA_ROOT = '/var/www/statics/oferclub/media'


FACEBOOK_APP_ID = '340736239438743'
FACEBOOK_APP_SECRET = 'eac89cdcf746cbb69397be018ccaf071'
FACEBOOK_CALLBACK_URL = 'http://ofer.gloose.me/new/facebook/callback/'

