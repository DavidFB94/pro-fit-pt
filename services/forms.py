from django import forms
from django.core.validators import MinValueValidator
from django.forms import modelformset_factory
from .models import Service, Category, PricingTier


class ServiceForm(forms.ModelForm):
    pricing_tiers = forms.ModelMultipleChoiceField(
        queryset=PricingTier.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )

    class Meta:
        model = Service
        fields = ['name', 'category', 'description', 'image', 'pricing_tiers']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        category_choices = [(c.id, c.name) for c in categories]
        self.fields['category'].choices = category_choices
        for field in self.fields.values():
            field.widget.attrs['class'] = 'border-color'
