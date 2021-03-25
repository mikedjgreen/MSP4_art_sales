from django.contrib import admin
from .models import Members


class MembersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'email_address',
        'created_at',
        'bio',
        'username',
    )

    ordering = ('full_name',)


admin.site.register(Members, MembersAdmin)
