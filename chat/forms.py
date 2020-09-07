from django import forms
from django.contrib.auth import get_user_model
from web_auth.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('message',)