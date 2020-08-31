from django import forms
from web_auth.models import Pet


class PetCreationForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'avatar',)
