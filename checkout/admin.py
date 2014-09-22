from django.contrib import admin
from checkout.models import Coupon, Order, Operation

class CouponInline(admin.StackedInline):
    model = Coupon

class OrderAdmin(admin.ModelAdmin):
    
    list_display = ('user', 'total', 'status', 'purchase_time')
    search_fields = ('user__full_name',)
    date_hierarchy = 'purchase_time'
    ordering = ('-purchase_time',)
    readonly_fields = ('purchase_time',)

    inlines = [
	    CouponInline,
	]

class CouponAdmin(admin.ModelAdmin):
    
    list_display = ('name_consumer', 'code', 'price', 'is_consumed')
    search_fields = ('name_consumer', 'code', )
    date_hierarchy = 'date_created'
    ordering = ('-date_created',)
    readonly_fields = ('date_created',)

class OperationAdmin(admin.ModelAdmin):
    
    list_display = ('user', 'type_operation', 'value', 'created_at')
    search_fields = ('user__full_name', )
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)

admin.site.register(Order, OrderAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(Operation, OperationAdmin)
