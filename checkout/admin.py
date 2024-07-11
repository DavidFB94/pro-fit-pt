from django.contrib import admin
from .models import Order, OrderLineItem, PricingTier


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'grand_total', 'original_cart',
                       'stripe_pid')

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'grand_total',
              'original_cart', 'stripe_pid')

    list_display = ('order_number', 'date',
                    'full_name', 'grand_total',)

    ordering = ('-date',)


class OrderLineItemAdmin(admin.ModelAdmin):
    list_display = ('service', 'get_quantity', 'get_price_per_unit')

    def get_quantity(self, obj):
        return obj.pricingtier.quantity if obj.pricingtier else 'N/A'
    get_quantity.short_description = 'Quantity'

    def get_price_per_unit(self, obj):
        return obj.pricingtier.price_per_unit if obj.pricingtier else 'N/A'
    get_price_per_unit.short_description = 'Price per Unit'


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLineItem, OrderLineItemAdmin)
