from django import forms
from django.core.validators import MinValueValidator
from .models import Service, Category, PricingTier


class ServiceForm(forms.ModelForm):
    pricing_tiers = forms.ModelMultipleChoiceField(
        queryset=PricingTier.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )

    class Meta:
        model = Service
        fields = ['name', 'category', 'description', 'pricing_tiers', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        category_choices = [(c.id, c.name) for c in categories]

        self.fields['name'].widget.attrs['autofocus'] = True
        self.fields['category'].choices = category_choices
        for field in self.fields.values():
            field.widget.attrs['class'] = 'border-color'
        self.fields['image'].required = False
        self.fields['image'].label = 'Image'

        self.fields['pricing_tiers'].queryset = (
            PricingTier.objects.all().order_by('quantity')
            )

        if self.instance and self.instance.pk and self.instance.image:
            self.fields['delete_image'] = (
                forms.BooleanField(required=False, label='Delete image')
                )
