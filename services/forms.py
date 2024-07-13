from django import forms
from django.core.validators import MinValueValidator
from django.forms import inlineformset_factory
from .models import Service, Category, PricingTier


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'category', 'description', 'image']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        category_choices = [(c.id, c.name) for c in categories]
        self.fields['category'].choices = category_choices
        
        for field in self.fields.values():
            field.widget.attrs['class'] = 'border-black rounded-0'

