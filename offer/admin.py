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

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.readonly_fields

        if self.declared_fieldsets:
            return flatten_fieldsets(self.declared_fieldsets)
        else:
            return list(set(
                [field.name for field in self.opts.local_fields] +
                [field.name for field in self.opts.local_many_to_many]
            ))

    def get_queryset(self, request):
        qs = super(OptionInline, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(filial=request.user)

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

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.readonly_fields

        if self.declared_fieldsets:
            return flatten_fieldsets(self.declared_fieldsets)
        else:
            return list(set(
                [field.name for field in self.opts.local_fields] +
                [field.name for field in self.opts.local_many_to_many]
            ))

    def get_queryset(self, request):
        # import pdb;pdb.set_trace()
        qs = super(OfferAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(options__filial=request.user)


admin.site.register(Offer, OfferAdmin)
admin.site.register(Category)
