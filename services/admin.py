from django.contrib import admin
from .models import Service, Category, PricingTier

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'description',
    )

    ordering = ('category',)


class PricingTierAdmin(admin.ModelAdmin):
    list_display = (
        'service',
        'quantity',
        'price_per_unit',
    )

    ordering = ('service',)


admin.site.register(Service, ServiceAdmin)
admin.site.register(Category)
admin.site.register(PricingTier, PricingTierAdmin)
