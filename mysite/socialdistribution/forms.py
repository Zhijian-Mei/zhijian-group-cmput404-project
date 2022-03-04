from django import forms
from .models import AuthorModel


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = AuthorModel
        fields = ['displayName']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = AuthorModel
        fields = ['profileImage']
