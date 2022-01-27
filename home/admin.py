from django.contrib import admin
from .models import ContactUs

# Register your models here.
class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'message',
        'date',
        'email',
    )

admin.site.register(ContactUs, ContactUsAdmin)