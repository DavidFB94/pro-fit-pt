from django.contrib import admin
from .models import Contact

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'message',
        'read',
    )
    list_display_links = ('name',)
    list_editable = ('read',)

    ordering = ('name',)


admin.site.register(Contact, ContactAdmin)
