from django import forms
from .models import Artworks
from .widgets import CustomClearableFileInput


class ArtworkForm(forms.ModelForm):

    class Meta:
        model = Artworks
        fields = ('title', 'artist', 'description',
                  'price', 'sold',
                  'height', 'width', 'depth',
                  'image',)

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ArtworkEditForm(forms.ModelForm):

    class Meta:
        model = Artworks
        fields = ('title', 'artist', 'description',
                  'category',
                  'price', 'sold',
                  'height', 'width', 'depth',
                  'image',)

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
