from decimal import Decimal
from django.conf import settings
def get_price_per_unit(service, quantity):
    """ Cart_contents helper function to access price_per_unit """
    pricing_tier = PricingTier.objects.filter(service=service, quantity__lte=quantity).order_by('-quantity').first()
    if pricing_tier:
        return pricing_tier.price_per_unit

def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0

    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context