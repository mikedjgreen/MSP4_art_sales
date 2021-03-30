from django.db import models
from django.conf import settings
from django.db.models.functions import Now
from django.db.models.functions import TruncYear


class Members(models.Model):

    class Meta:
        verbose_name_plural = "Members"

    full_name = models.CharField(max_length=254, null=False, blank=False)
    email_address = models.EmailField(max_length=254, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(blank=True)
    username = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.full_name


class Subs(models.Model):
    """ Memebrship Subscriptions table """
    class Meta:
        verbose_name_plural = "Subs"

    year = models.IntegerField(blank=False, help_text='2021 onwards')
    username = models.CharField(max_length=254, blank=False)
    paid = models.DecimalField(max_digits=6, decimal_places=2)
    date_paid = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set paid subscription.
        """
        self.paid = settings.CLUB_SUBSCRIPTION
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.username} {self.year}'
