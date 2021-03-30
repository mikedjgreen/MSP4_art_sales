from django import forms
from .models import Members, Subs


class MemberForm(forms.ModelForm):

    class Meta:
        model = Members
        fields = ('full_name',
                  'email_address',
                  'bio',
                  'username',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SubsForm(forms.ModelForm):

    class Meta:
        model = Subs
        fields = ('year',
                  'username',
                  'paid',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
