import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from artworks.models import Artworks
#  Orders and OrderItems


class Orders(models.Model):

    class Meta:
        verbose_name_plural = "Orders"

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_id = models.IntegerField()
    # entries for anonymous buyer, not patron
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, blank=True)
    county = models.CharField(max_length=80, blank=True)
    # totals
    delivery = models.DecimalField(max_digits=6,
                                   decimal_places=2,
                                   null=False, default=0)
    commission = models.DecimalField(max_digits=6,
                                     decimal_places=2,
                                     null=False, default=0)
    vat = models.DecimalField(max_digits=6,
                              decimal_places=2,
                              null=False, default=0)
    total = models.DecimalField(max_digits=6,
                                decimal_places=2,
                                null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    original_basket = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for VAT and commission.
        """
        self.total = self.lineitems.aggregate(Sum('line_total'))['line_total_sum'] or 0
        self.vat = self.total * settings.VAT_PERCENTAGE / 100
        self.commission = self.total * settings.COMMISSION_PERCENTAGE / 100
        self.delivery = self.total * settings.DELIVERY_PERCENTAGE / 100
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderItems(models.Model):
    order_number = models.ForeignKey(Orders, null=False, blank=False,
                                     on_delete=models.CASCADE,
                                     related_name='lineitems')
    line_number = models.IntegerField(null=False, blank=False, unique=True)
    artworks = models.ForeignKey(Artworks, null=False,
                                 blank=False,
                                 on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(default=1)  # for cards, prints, etc
    line_total = models.DecimalField(max_digits=6, decimal_places=2,
                                     null=False,
                                     blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.line_total = self.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number, self.line_number
