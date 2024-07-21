from django.contrib import admin
from .models import FAQs, Newsletter

# Register your models here.
class FAQsAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'answer',
    )

    ordering = ('question',)

admin.site.register(FAQs, FAQsAdmin)

class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        'email',
    )

    ordering = ('email',)

admin.site.register(Newsletter, NewsletterAdmin)