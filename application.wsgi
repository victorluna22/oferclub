# file configuration of apache mod_wsgi
from django.conf import settings
import os, sys, site
from os.path import abspath, join, dirname
project_name = "oferclub"
root_dir = abspath(join(dirname(__file__), '..'))
sys.path.append(root_dir)
#sys.path.append(join(root_dir, project_name))
os.environ["DJANGO_SETTINGS_MODULE"]= 'settings.homolog'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
