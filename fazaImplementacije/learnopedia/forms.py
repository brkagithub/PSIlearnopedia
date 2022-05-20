from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms
from django.forms import ModelForm, Form, RadioSelect


class KorisnikCreationForm(UserCreationForm):

    class Meta:
        model = Korisnik
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name']


class SearchForm(Form):
    filter = forms.CharField(max_length=50)


class UpdateUserForm(Form):
    username = forms.CharField(max_length=50, label="Username")
    firstName = forms.CharField(max_length=50, label="First Name")
    lastName = forms.CharField(max_length=50, label="Last Name")
    description = forms.CharField(widget=forms.Textarea, label="Description")


class QuestionForm(Form):
    Question = forms.CharField(max_length=50)
    Answer1 = forms.CharField(max_length=50)
    Answer2 = forms.CharField(max_length=50)
    Answer3 = forms.CharField(max_length=50)
    Answer4 = forms.CharField(max_length=50)
    #widget =  forms.RadioSelect(choices=TACNI_ODGOVORI)
    choice = forms.ChoiceField(widget=RadioSelect(), choices=[(1, 'Answer1'), (2, 'Answer2'),(3,'Answer3'),(4,'Answer4')])

class Testiranje(Form):
    answers = forms.ChoiceField(widget=RadioSelect(), choices=[('answer1', ""), ('answer2', ""), ('answer3', ""), ('answer4', "")])

