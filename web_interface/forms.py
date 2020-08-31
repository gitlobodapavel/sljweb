from django import forms
from web_auth.models import Pet, Product, ProductImage
from django.contrib.auth import get_user_model


class PetCreationForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'avatar',)


class EditUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'avatar', 'bio', 'status')


class PlaceProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('image', 'title', 'description', 'price')


class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('image', 'title', 'description', 'price')