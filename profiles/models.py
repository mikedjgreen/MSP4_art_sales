from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class Patron(models.Model):
    """
    A user profile model called Patron, for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, blank=True)
    default_email = models.EmailField(max_length=254, blank=False)
    default_street_address1 = models.CharField(max_length=80, blank=True)
    default_street_address2 = models.CharField(max_length=80, blank=True)
    default_town_or_city = models.CharField(max_length=40, blank=True)
    default_county = models.CharField(max_length=80, blank=True)
    default_postcode = models.CharField(max_length=20, blank=True)
    default_country = CountryField(blank_label='Country *', blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_patron(sender, instance, created, **kwargs):
    """
    Create or update the user profile (Patron)
    """
    if created:
        Patron.objects.create(user=instance)
    # Existing users: just save the profile
    instance.patron.save()
