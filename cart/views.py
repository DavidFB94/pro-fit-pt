from django.contrib import messages
from services.models import Service, PricingTier
from django.shortcuts import (
    render, redirect, HttpResponse, get_object_or_404
    )

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
    service = get_object_or_404(Service, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    # Get service_quantity from POST data
    service_quantity = request.POST.get('service_quantity')
    if not service_quantity:
        messages.error(request, 'Please select a valid quantity.')
        return redirect(redirect_url)
    try:
        pricing_tier_id = int(service_quantity)
    except (ValueError, TypeError):
        messages.error(request, 'Invalid quantity selected.')
        return redirect(redirect_url)

    pricing_tier = get_object_or_404(PricingTier, id=pricing_tier_id)

    # Composite key using item_id and pricing_tier_id
    composite_key = f"{item_id}_{pricing_tier.id}"

    if composite_key in cart:
        cart[composite_key]['quantity'] += pricing_tier.quantity
        messages.success(
            request,
            f'Added {pricing_tier.quantity}x more {service.name} '
            f'for ${pricing_tier.price_per_unit}/each to your cart')
    else:
        cart[composite_key] = {
            'quantity': pricing_tier.quantity,
            'service_id': item_id,
            'service_name': service.name,
            'pricing_tier_id': pricing_tier.id,
            'pricing_tier_quantity': pricing_tier.quantity,
            'price_per_unit': float(pricing_tier.price_per_unit)
        }
        messages.success(
            request,
            f'Added {pricing_tier.quantity}x {service.name} '
            f'for ${pricing_tier.price_per_unit}/each to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, composite_key):
    """
    Remove the item from the shopping cart
    """
    try:
        cart = request.session.get('cart', {})

        if composite_key in cart:
            service_name = cart[composite_key]['service_name']
            cart.pop(composite_key)
            messages.success(request, f'Removed {service_name} from your cart')
        else:
            messages.error(request, 'Item not found in cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
