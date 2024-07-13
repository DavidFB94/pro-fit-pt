from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Subquery, OuterRef
from django.core.paginator import Paginator
from django.db.models.functions import Lower

from .models import Service, PricingTier, Category
from .forms import ServiceForm, PricingTierForm, PricingTierFormSet


def all_services(request):
    """ A view to show all services in a paginated list, including sorting and search queries """

    query = None
    categories = None
    sort = 'name'  # initial sort field as 'name'
    direction = 'asc'  # initial sort direction as 'asc'

    # subquery to get the highest or lowest pricing tier for each service
    highest_pricing_tier = PricingTier.objects.filter(
        service=OuterRef('pk')
    ).order_by('-price_per_unit').values('price_per_unit')[:1]
    
    lowest_pricing_tier = PricingTier.objects.filter(
        service=OuterRef('pk')
    ).order_by('price_per_unit').values('price_per_unit')[:1]

    # fetch all services
    services = Service.objects.all()

    # handle sorting, filtering, and searching
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                services = services.annotate(lower_name=Lower('name'))
            elif sortkey == 'pricingtier':
                direction = request.GET.get('direction', 'asc')
                if direction == 'asc':
                    services = services.annotate(lowest_price=Subquery(lowest_pricing_tier))
                    sortkey = 'lowest_price'
                else:
                    services = services.annotate(highest_price=Subquery(highest_pricing_tier))
                    sortkey = 'highest_price'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            services = services.order_by(sortkey)
        else:
            services = services.order_by('name')

        if 'category' in request.GET:
            category_names = request.GET['category'].split(',')
            categories = Category.objects.filter(name__in=category_names)
            services = services.filter(category__name__in=category_names)
        
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('services'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            services = services.filter(queries)

    # apply distinct after filtering/sorting to get unique services only
    services = services.distinct()

    total_services_count = services.count()  # Get the total count

    current_sorting = f'{sort}_{direction}'

    paginator = Paginator(services, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'services': page_obj.object_list,
        'page_obj': page_obj,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'query': query,
        'categories': category_names if categories else None,
        'sort': sort,
        'direction': direction,
        'total_services_count': total_services_count,
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


@login_required
def add_service(request):
    """ Add a service to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        formset = PricingTierFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            service = form.save()
            formset.instance = service
            formset.save()
            messages.success(request, 'Successfully added service!')
            return redirect(reverse('service_details', args=[service.id]))
        else:
            messages.error(request, 'Failed to add service. Please ensure the form is valid.')
    else:
        form = ServiceForm()
        formset = PricingTierFormSet()

    template = 'services/add_service.html'
    context = {
        'form': form,
        'formset': formset,
    }

    return render(request, template, context)


@login_required
def edit_service(request, service_id):
    """ Edit a service in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    service = get_object_or_404(Service, pk=service_id)
    formset = PricingTierFormSet(request.POST)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated service!')
            return redirect(reverse('service_detail', args=[service.id]))
        else:
            messages.error(request,
                           ('Failed to update service. '
                            'Please ensure the form is valid.'))
    else:
        form = ServiceForm(instance=service)
        messages.info(request, f'You are editing {service.name}')

    template = 'services/edit_service.html'
    context = {
        'form': form,
        'formset': formset,
        'service': service,
    }

    return render(request, template, context)


@login_required
def delete_service(request, service_id):
    """ Delete a service from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    service = get_object_or_404(Service, pk=service_id)
    service.delete()
    messages.success(request, 'Service deleted!')
    return redirect(reverse('services'))
