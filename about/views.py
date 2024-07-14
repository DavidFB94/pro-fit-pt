from django.shortcuts import render

# Create your views here.

def about(request):
    """
    Display the about page, with FAQs section
    """
    
    template = 'about/about.html'
    context = {}

    return render(request, template, context)
