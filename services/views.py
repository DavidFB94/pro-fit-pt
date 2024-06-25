from django.shortcuts import render
from .models import Service


def all_services(request):
    """ A view to show all products, including sorting and search queries """

    services = Service.objects.all()

    context = {
        'all_services': services,
    }

    return render(request, 'services/services.html', context)