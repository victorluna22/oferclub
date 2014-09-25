# coding: utf-8
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from offer.models import Offer, Category, Option, Image
from django import forms
from tinymce.widgets import TinyMCE

class OptionInline(admin.StackedInline):
    model = Option
    min_num = 1
    extra = 0

class ImageInline(admin.TabularInline):
    model = Image
    min_num = 1
    extra = 1

class OfferForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Offer
        fields = ('title', 'slug', 'highlight', 'highlight_image', 'affiliate', 'bought', 'bought_virtual', 'max_by_user', 'percent_by_site',
        		'percent_cashback', 'city', 'description', 'regulation')

class OfferAdmin(admin.ModelAdmin):

	form = OfferForm
	list_display = ('title', 'percent_by_site', 'bought', 'date_created')
	search_fields = ('title',)
	date_hierarchy = 'date_created'
	ordering = ('-date_created',)
	readonly_fields = ('date_created', 'bought', 'slug')
	inlines = [
	    ImageInline,
	    OptionInline,
	]



admin.site.register(Offer, OfferAdmin)
admin.site.register(Category)
