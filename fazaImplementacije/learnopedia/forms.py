from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms
from django.forms import ModelForm,Form

class KorisnikCreationForm(UserCreationForm):

    class Meta:
        model = Korisnik
        fields = ['username', 'password1', 'password2']


class SearchForm(Form):
    filter = forms.CharField(max_length=50)