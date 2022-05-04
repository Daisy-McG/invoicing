from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'client',
        'address_line_one',
        'address_line_two',
        'county',
        'country',
        'paid_to_date',
        'balance',
        'email',
    )

admin.site.register(Client, ClientAdmin)