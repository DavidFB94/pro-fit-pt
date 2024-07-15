from django.contrib import admin
from django.utils.safestring import mark_safe
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
        'get_services',
        'quantity',
        'price_per_unit',
    )

    def get_services(self, object):
        return mark_safe('<br>'.join(
            [
                service.name for service in object.services.all()
            ]
        ))
    get_services.short_description = 'Services'


admin.site.register(Service, ServiceAdmin)
admin.site.register(Category)
admin.site.register(PricingTier, PricingTierAdmin)
