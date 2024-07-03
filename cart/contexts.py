from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from services.models import Service, PricingTier

def get_price_per_unit(service, quantity):
    """ Cart_contents helper function to access price_per_unit """
    pricing_tier = PricingTier.objects.filter(service=service, quantity__lte=quantity).order_by('-quantity').first()
    if pricing_tier:
        return pricing_tier.price_per_unit

def cart_contents(request):

    cart_items = []
    total = 0
    service_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        service = get_object_or_404(Service, pk=item_id)
        price_per_unit = get_price_per_unit(service, quantity)

        total += quantity * price_per_unit
        service_count += quantity

        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'service': service,
        })

    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'service_count': service_count,
        'grand_total': grand_total,
    }

    return context
