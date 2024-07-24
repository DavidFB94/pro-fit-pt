from django.shortcuts import get_object_or_404
from services.models import Service, PricingTier


def get_price_per_unit(service, quantity):
    """ Cart_contents helper function to access price_per_unit """
    pricing_tier = PricingTier.objects.filter(
         service=service, quantity__lte=quantity).order_by('-quantity').first()
    if pricing_tier:
        return pricing_tier.price_per_unit


def cart_contents(request):
    cart_items = []
    total = 0
    service_count = 0
    cart = request.session.get('cart', {})

    for composite_key, item_data in cart.items():
        item_id, pricing_tier_id = composite_key.split('_')
        item_id = int(item_id)
        pricing_tier_id = int(pricing_tier_id)

        service = get_object_or_404(Service, pk=item_id)
        pricing_tier = get_object_or_404(PricingTier, pk=pricing_tier_id)
        quantity = item_data['quantity']
        price_per_unit = pricing_tier.price_per_unit

        total += quantity * price_per_unit
        service_count += quantity

        cart_items.append({
            'composite_key': composite_key,
            'item_id': item_id,
            'quantity': quantity,
            'service': service,
            'pricing_tier': pricing_tier,
            'price_per_unit': price_per_unit,
        })

    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'service_count': service_count,
        'grand_total': grand_total,
    }

    return context
