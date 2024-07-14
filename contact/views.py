from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

# Create your views here.

def contact(request):
    """
    Display the contact page and save contact form
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            message.success(request, 'Your message has been sent!')
            return redirect('contact')
        else:
            messages.error(request,
                           ('Failed to send message. '
                            'Please ensure the form is valid.'))
    else:
        form = ContactForm()
    
    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
