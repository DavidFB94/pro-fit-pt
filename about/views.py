from django.shortcuts import render, redirect
from django.contrib import messages
from .models import FAQs
from .forms import NewsletterForm

# Create your views here.


def about(request):
    """
    Display the about page with about us section,
    FAQs section and newsletter signup
    """
    faqs = FAQs.objects.all()

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have subscribed to our newsletter!')
            return redirect('about')
        else:
            messages.error(
                request, 'Failed to sign up. Please ensure the form is valid.')
    else:
        form = NewsletterForm()

    template = 'about/about.html'
    context = {
        'faqs': faqs,
        'form': form,
    }

    return render(request, template, context)
