# -*- coding: utf-8 -*-

from django import template

register = template.Library()


@register.filter
def titulo_bloco(bloco):
    return bloco['titulo_bloco']


@register.filter
def qtd(bloco):
    return len(bloco['ofertas'])

