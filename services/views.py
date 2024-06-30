from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Service, PricingTier


def all_services(request):
    """ A view to show all services in a paginated list """
    # Fetch distinct services, ordered by name
    services = Service.objects.all().distinct().order_by('name')
    query = None


    # From CI Boutique Ado walkthrough
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('services'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            services = services.filter(queries)


    paginator = Paginator(services, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    services_list = []
    for service in page_obj:
        pricing_tier = PricingTier.objects.filter(service=service).order_by('-price_per_unit').first()
        services_list.append((service, pricing_tier))
    

    context = {
        'services_list': services_list,
        'page_obj': page_obj,
        'search_term': query,
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


