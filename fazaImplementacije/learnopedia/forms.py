from django.contrib.auth.forms import UserCreationForm
from .models import *


class KorisnikCreationForm(UserCreationForm):

    class Meta:
        model = Korisnik
        fields = ['username', 'password1', 'password2']