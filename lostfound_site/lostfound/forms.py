from django import forms
from .models import LostItem, FoundItem


class LostItemForm(forms.ModelForm):
    class Meta:
        model = LostItem
        fields = ['type', 'description', 'location']


class FoundItemForm(forms.ModelForm):
    class Meta:
        model = FoundItem
        fields = ['type', 'description', 'location', 'contact', 'email']

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']