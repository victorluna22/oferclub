from django.contrib import admin
from checkout.models import Coupon, Order, Operation
from django.contrib.admin.util import flatten_fieldsets

class CouponInline(admin.StackedInline):
    model = Coupon
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

class OrderAdmin(admin.ModelAdmin):
    
    list_display = ('user', 'total', 'status', 'purchase_time')
    search_fields = ('user__full_name',)
    date_hierarchy = 'purchase_time'
    ordering = ('-purchase_time',)
    readonly_fields = ('purchase_time',)

    inlines = [
	    CouponInline,
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

class CouponAdmin(admin.ModelAdmin):
    
    list_display = ('name_consumer', 'code', 'price', 'is_consumed')
    search_fields = ('name_consumer', 'code', )
    date_hierarchy = 'date_created'
    ordering = ('-date_created',)
    readonly_fields = ('date_created',)

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
