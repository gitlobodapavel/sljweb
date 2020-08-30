from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=70, help_text='Required')

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class LoginForm(forms.ModelForm):

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'placeholder': 'email *'
    }))

    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'placeholder': 'password *'
    }))

    class Meta:
        model = get_user_model()
        fields = ('email', 'password')