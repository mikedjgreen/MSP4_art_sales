from django.contrib import admin
from .models import Members, Subs


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


class SubsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'year',
        'username',
        'paid',
        'date_paid',
    )

    ordering = ('username', 'year',)


admin.site.register(Subs, SubsAdmin)
