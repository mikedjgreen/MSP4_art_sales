from django import forms
from .models import Artworks
from .widgets import CustomClearableFileInput


class ArtworkForm(forms.ModelForm):

    class Meta:
        model = Artworks
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
