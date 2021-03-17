from django.contrib import admin
from .models import Orders, OrderItems


class OrderItemsAdminInline(admin.TabularInline):
    model = OrderItems
    readonly_fields = ('line_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemsAdminInline,)

    readonly_fields = ('order_number', 'created_at',
                       'delivery', 'total',
                       'commission', 'vat')

    fields = ('order_number', 'created_at', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery',
              'commission', 'vat', 'total',)

    list_display = ('order_number', 'created_at', 'full_name',
                    'commission', 'delivery', 'vat',
                    'total',)

    ordering = ('-created_at',)


admin.site.register(Orders, OrderAdmin)
