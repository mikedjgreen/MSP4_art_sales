from django.db import models
from django.utils.translation import gettext_lazy as _
from members.models import Members


class art_category(models.TextChoices):
    PAINTING = 'PA', _('Painting')
    DRAWING = 'DR', _('Drawing')
    CERAMIC = 'CE', _('Ceramics')
    SCULPTURE = 'SC', _('Sculpture')
    PRINTS = 'PR', _('Prints')
    CARDS = 'CA', _('Cards')
    BOOKS = 'BO', _('Books')
    MIXED = 'MX', _('Mixed')

    def __str__(self):
        return self.label


class Artworks(models.Model):

    class Meta:
        verbose_name_plural = "Artworks"

    title = models.CharField(max_length=254)
    artist = models.ForeignKey(Members, on_delete=models.SET_NULL,
                               null=True,
                               blank=True, related_name='members')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sold = models.BooleanField(default=False)
    category = models.CharField(max_length=2,
                                choices=art_category.choices,
                                default=art_category.PAINTING)
    created_at = models.DateTimeField(auto_now_add=True)
    image_path = models.URLField(max_length=1024, blank=True)
    height = models.DecimalField(max_digits=6, decimal_places=2)
    width = models.DecimalField(max_digits=6, decimal_places=2)
    depth = models.DecimalField(max_digits=6, decimal_places=2,
                                null=True, blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title
