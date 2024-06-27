from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Service, PricingTier


def all_services(request):
    services = Service.objects.all()
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
