"""
Django settings for oferclub project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

FILE_UPLOAD_PERMISSIONS = 0777
FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0777


# SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x*s0a%+l%j0^c^gg6+@6-fp(t^8-jl9*94pv0#a^44ifsrih%_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

THUMBNAIL_DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'account.OferClubAbstractUser'

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'

FACEBOOK_APP_ID = '340736239438743'
FACEBOOK_APP_SECRET = 'eac89cdcf746cbb69397be018ccaf071'
FACEBOOK_CALLBACK_URL = 'http://localhost:8000/new/facebook/callback/'

# SITE_ID = 1
SLUGFIELD_SEPARATOR = ''

LANGUAGE_CODE = 'pt-BR'
LANGUAGES_CODE = ['pt-BR']

DEFAULT_FROM_EMAIL = 'victorluna22@gmail.com'

# Application definition


INSTALLED_APPS = (
    'django.contrib.contenttypes',
    # 'django_admin_bootstrapped.bootstrap3',
    # 'django_admin_bootstrapped',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sorl.thumbnail',
    'tinymce',
    'account',
    'checkout',
    'offer',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    )

MIDDLEWARE_CLASSES = (
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'offer.middleware.CitiesMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'

AUTHENTICATION_BACKENDS = (
    'account.backends.AccountsBackend.AccountsBackend',
    'account.backends.EmailBackend.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
    # 'guardian.backends.ObjectPermissionBackend',  # activate django-guardian
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/


TIME_ZONE = 'America/Recife'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/home/victor/projetos/oferclub/static'

MEDIA_URL = '/media/'

MEDIA_ROOT = '/var/www/oferclub/media'
# MEDIA_ROOT = '/home/gloose-onix/projetos/oferclub/media'

SEND_EMAIL = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USER = 'victorluna22@gmail.com'
EMAIL_PASSWORD = 'v183729465'
EMAIL_PORT = 487
EMAIL_TLS = False

if DEBUG:
    EMAIL_HOST = '127.0.0.1'
    EMAIL_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_PORT = 1025
    EMAIL_USE_TLS = True

if SEND_EMAIL:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = EMAIL_HOST
    EMAIL_HOST_USER = EMAIL_USER
    EMAIL_HOST_PASSWORD = EMAIL_PASSWORD
    EMAIL_PORT = EMAIL_PORT
    EMAIL_USE_TLS = EMAIL_TLS
    SERVER_EMAIL = EMAIL_HOST_USER
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


TINYMCE_JS_URL = os.path.join(STATIC_URL, "tiny_mce/tiny_mce.js")
TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, "tiny_mce")

# TINYMCE_JS_URL = 'http://debug.example.org/tiny_mce/tiny_mce_src.js'
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}
TINYMCE_SPELLCHECKER = True
TINYMCE_COMPRESSOR = True