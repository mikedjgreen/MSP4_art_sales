from django.contrib import admin
from .models import Orders, OrderItems


class OrderItemsAdminInline(admin.TabularInline):
    model = OrderItems
    readonly_fields = ('line_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemsAdminInline,)

    readonly_fields = ('order_number', 'created_at',
                       'delivery', 'total',
                       'commission', 'vat',
                       'original_basket',
                       'stripe_pid')

    fields = ('order_number', 'user_profile', 'created_at', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery',
              'commission', 'vat', 'total',
              'original_basket',
              'stripe_pid')

    list_display = ('order_number', 'created_at', 'full_name',
                    'commission', 'delivery', 'vat',
                    'total',)

    ordering = ('-created_at',)


admin.site.register(Orders, OrderAdmin)
