from django import forms
from .models import Artworks, art_category


class ArtworkForm(forms.ModelForm):

    class Meta:
        model = Artworks
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
