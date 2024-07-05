from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from services.models import Service

# Create your views here.

def view_cart(request):
    """
    A view that renders the bag contents page
    """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    Add a quantity of the specified service to the shopping cart
    """

    service = Service.objects.get(pk=item_id)
    quantity = int(request.POST.get('service_quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {service.name} to your cart')
    
    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """
    Remove the item from the shopping cart
    """
    try:
        cart = request.session.get('cart', {})

        if item_id in cart:
            cart.pop(item_id)
        
        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
