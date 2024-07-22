from django.db import models
from cloudinary.models import CloudinaryField

import cloudinary


# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Service(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    image = cloudinary.models.CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name


class PricingTier(models.Model):
    services = models.ManyToManyField(Service, related_name='pricing_tiers', blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    price_per_unit = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Package {self.quantity} - {self.price_per_unit}$/unit - total: {self.price_per_unit*self.quantity}$"
