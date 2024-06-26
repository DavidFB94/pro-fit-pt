from django.shortcuts import render
from .models import Service, PricingTier

def all_services(request):
    services = Service.objects.all()
    services_with_pricing = []

    for service in services:
        pricing_tier = PricingTier.objects.filter(service=service).first()
        services_with_pricing.append((service, pricing_tier))

    context = {
        'services_with_pricing': services_with_pricing,
    }

    return render(request, 'services/services.html', context)
