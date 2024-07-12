from django import forms
from django.core.validators import MinValueValidator
from .models import Service, Category, PricingTier


class ServiceForm(forms.ModelForm):
    quantity = forms.IntegerField(
        required=True,
        validators=[MinValueValidator(1)],
    )
    price_per_unit = forms.DecimalField(
        max_digits=6,
        decimal_places=2,
        required=True,
        validators=[MinValueValidator(0.01)],
    )

    class Meta:
        model = Service
        fields = ['name', 'category', 'description', 'quantity', 'price_per_unit', 'image',]
        exclude = ['pricingtier_set']  # Exclude related PricingTier objects if there is a reverse relation

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        category_choices = [(c.id, c.name) for c in categories]
        self.fields['category'].choices = category_choices

        self.fields['quantity'].widget.attrs['class'] = 'border-black rounded-0'
        self.fields['price_per_unit'].widget.attrs['class'] = 'border-black rounded-0'

        for field_name, field in self.fields.items():
            if field_name not in ['quantity', 'price_per_unit']:
                field.widget.attrs['class'] = 'border-black rounded-0'
