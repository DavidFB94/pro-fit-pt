from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator

from .models import Service, PricingTier


def all_services(request):
    services = Service.objects.all().order_by('-pricingtier')
    services_list = []
    
    paginator = Paginator(services, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    for service in page_obj:
        pricing_tier = PricingTier.objects.filter(service=service).first()
        services_list.append((service, pricing_tier))

    context = {
        'services_list': services_list,
        "page_obj": page_obj,
    }

    return render(request, 'services/services.html', context)


def service_details(request, service_id):
    """ A view to show individual service details """

    service = get_object_or_404(Service, pk=service_id)
    pricing_tiers = PricingTier.objects.filter(service=service)


    context = {
        'service': service,
        'pricing_tiers': pricing_tiers,
    }

    return render(request, 'services/service_details.html', context)


