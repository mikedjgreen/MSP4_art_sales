from django.contrib import admin
from .models import Patron


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
            'user',
            'default_phone_number',
            'default_email',
            'default_country',
            'default_postcode',
            'default_town_or_city',
            'default_street_address1',
            'default_street_address2',
            'default_county'
    )

    ordering = ('user',)


admin.site.register(Patron, ProfileAdmin)
