from django import forms
from .models import Members


class MemberForm(forms.ModelForm):

    class Meta:
        model = Members
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
