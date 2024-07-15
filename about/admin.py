from django.contrib import admin
from .models import FAQs

# Register your models here.
class FAQsAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'answer',
    )

    ordering = ('question',)

admin.site.register(FAQs, FAQsAdmin)
