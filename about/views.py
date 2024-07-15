from django.shortcuts import render
from .models import FAQs

# Create your views here.

def about(request):
    """
    Display the about page, with FAQs section
    """
    faqs = FAQs.objects.all()

    template = 'about/about.html'
    context = {
        'faqs': faqs,
    }

    return render(request, template, context)
