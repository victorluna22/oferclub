# coding: utf-8
from datetime import datetime
from django.contrib import admin
from django import forms
from checkout.models import Coupon, Order, Operation, CONSUMED
from django.contrib.admin.util import flatten_fieldsets

class CouponInline(admin.StackedInline):
    model = Coupon
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    
    list_display = ('user', 'total', 'status', 'purchase_time')
    search_fields = ('user__full_name',)
    list_filter = ('user__date_joined',)
    date_hierarchy = 'purchase_time'
    ordering = ('-purchase_time',)
    readonly_fields = ('purchase_time',)

    inlines = [
	    CouponInline,
	]

class CouponForm(forms.ModelForm):
    model = Coupon

class CouponValidationForm(forms.ModelForm):
    code_validation = forms.CharField(
                        label=u'Código',
                        max_length=254,
                        widget=forms.TextInput(
                            attrs={'class': 'form-control validaTxt',
                                   'placeholder': 'CÓDIGO DO CUPOM' }),
                        help_text=u'Digite o código do cupom para que ele seja consumido.')
    model = Coupon

    def clean_code_validation(self):
        # import pdb;pdb.set_trace()
        if self.cleaned_data['code_validation'] and self.cleaned_data['code_validation'].upper() == self.instance.code:
            return self.cleaned_data['code_validation']
        else:
            raise forms.ValidationError('Código Inválido!')

    def save(self, commit=True):
        coupon = super(CouponValidationForm, self).save(commit=False)
        coupon.is_consumed = CONSUMED
        coupon.date_consumed = datetime.today()
        if commit:
            coupon.save()
        return coupon



class CouponAdmin(admin.ModelAdmin):
    
    list_display = ('order', 'price', 'is_consumed')
    search_fields = ('order__name_consumer', )
    date_hierarchy = 'date_created'
    ordering = ('-date_created',)
    readonly_fields = ('code', 'price', 'date_created')

    def get_readonly_fields(self, request, obj=None):
        # import pdb;pdb.set_trace()
        if request.user.is_superuser:
            self.form = CouponForm
            return self.readonly_fields
        if self.declared_fieldsets:
            return flatten_fieldsets(self.declared_fieldsets)
        else:
            fields = list(set(
                [field.name for field in self.opts.local_fields] +
                [field.name for field in self.opts.local_many_to_many]
            ))
            
            fields.remove('code')
            fields.remove('order')
            self.exclude = ('code', 'order')
            self.form = CouponValidationForm
            return fields

    def get_queryset(self, request):
        qs = super(CouponAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(order__option__filial=request.user)

class OperationAdmin(admin.ModelAdmin):
    
    list_display = ('user', 'type_operation', 'value', 'created_at')
    search_fields = ('user__full_name', )
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)

    # def save_model(self, request, obj, form, change):
    #     # import pdb;pdb.set_trace()
    #     if not request.user.has_perm('operation.change_operation'):
    #         messages.error(request, 
    #             "The Parking Location field cannot be changed.")
    #     super(OperationAdmin, self).save_model(request, obj, form, change)


admin.site.register(Order, OrderAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(Operation, OperationAdmin)
