# -*- coding: utf-8 -*-
from django import template


register = template.Library()


@register.filter
def titulo_bloco(bloco):
    return bloco['titulo_bloco']


@register.filter
def qtd(bloco):
    return len(bloco['ofertas'])

@register.filter
def breadcrumb(request, offer=None):
	from ..models import Type, City, Category
	breadcrumb = "<p class=\"container\" id=\"bread-crumb\">"

	type = Type.objects.get(id=request.session.get('typeoffer'))
	breadcrumb += "<a href=\"%s\">%s</a>" % ("/selecionar/" + type.slug + "/", type.name)

	city = City.objects.get(id=request.session.get('city'))
	breadcrumb += "> <span>%s</span>" % (city.name)

	if request.GET.get('category'):
		category_slug = request.GET.get('category')
		category = Category.objects.filter(slug=category_slug)
		if category:
			category_name = category[0].name
		else:
			category_name = category_slug.replace("-", " ").title()
		url_category = "%s?category=%s" % (request.path, category_slug)
		breadcrumb += "> <a href=\"%s\" class=\"active-bread\">%s</a>" % (url_category, category_name)
	
	if offer:
		breadcrumb += "> <a href=\"%s\" class=\"active-bread\">%s</a>" % ("/oferta/%s/" % offer.slug, offer.title)

	return breadcrumb