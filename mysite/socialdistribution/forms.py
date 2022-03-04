from django import forms
from .models import AuthorModel


class UserUpdateForm(forms.Form):
    username = forms.CharField(max_length=100)


class ProfileUpdateForm(forms.Form):
    Image = forms.ImageField()