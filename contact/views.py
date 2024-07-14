from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def contact(request):
    """
    Display the contact page
    """
    form = ContactForm()
    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
