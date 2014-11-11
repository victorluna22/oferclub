#coding: utf-8
from datetime import datetime
from datetime import timedelta
from django.conf import settings
from account.models import City

class CitiesMiddleware(object):

	def process_request(self, request):
		if not request.session.get('cities'):
			queryset = City.objects.all()
			cities = []
			for city in queryset:
				cities.append({'id': city.id, 'name': city.name})
			request.session['cities'] = cities
		if not request.session.get('city'):
			request.session['city'] = 2 # recife
		# import pdb;pdb.set_trace()
		if not request.session.get('typeoffer'):
			request.session['typeoffer'] = 1 # Ofertas Locais

	# def process_template_response(self, request, response):
	# 	if not request.COOKIES.get('city'):
	# 		max_age = 365 * 24 * 60 * 60  #one year
	# 		expires = datetime.strftime(datetime.utcnow() + timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
	# 		response.set_cookie('city', 2, max_age=max_age, expires=expires, secure=settings.SESSION_COOKIE_SECURE or None)

	# 	if not request.COOKIES.get('typeoffer'):
	# 		max_age = 1 * 24 * 60 * 60  #one day
	# 		expires = datetime.strftime(datetime.utcnow() + timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
	# 		response.set_cookie('typeoffer', 1, max_age=max_age, secure=settings.SESSION_COOKIE_SECURE or None)
	# 	return response


        