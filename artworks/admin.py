from django.contrib import admin
from .models import Artworks


class ArtworksAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'artist_id',
        'description',
        'price',
        'sold',
        'category',
        'created_at',
        'image_path',
        'height',
        'width',
        'depth',
        'image'
    )

    ordering = ('title',)


admin.site.register(Artworks, ArtworksAdmin)
