from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms

from django.forms import ModelForm, Form, RadioSelect
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


from django.forms import ModelForm,Form
from django.forms import ModelForm, TextInput, EmailInput

#Dejan Draskovic
#form for registering new user
class KorisnikCreationForm(UserCreationForm):
    class Meta:
        model = Korisnik

        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'description', 'profilePic']

class UpdateUserForm(Form):
    username = forms.CharField(max_length=50, label="Username")
    firstName = forms.CharField(max_length=50, label="First Name")
    lastName = forms.CharField(max_length=50, label="Last Name")
    profilePic = forms.ImageField(required=False)
    description = forms.CharField(widget=forms.Textarea, label="Description")

#Rasa Stojanovic
class SearchForm(Form):
    validatedArticlesOnly = forms.BooleanField(required=False)
    filter = forms.CharField(max_length=50, required=False)


#Dejan Draskovic
#form for creating new comment
class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['text']

#Dejan Draskovic
#form for creating new category
class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'description']

#Rasa Stojanovic
class QuestionUpdateForm(Form):
    Points = forms.IntegerField()
    Question = forms.CharField(max_length=50)
    Answer1 = forms.CharField(max_length=50)
    Answer2 = forms.CharField(max_length=50)
    Answer3 = forms.CharField(max_length=50)
    Answer4 = forms.CharField(max_length=50)
    choice = forms.ChoiceField(widget=RadioSelect(),choices=[(1, 'Answer1'), (2, 'Answer2'), (3, 'Answer3'), (4, 'Answer4')])

    def put(self, q, a1, a2, a3, a4, odgovor):
        self.Question = q
        self.Answer1 = a1;self.Answer2 = a1;self.Answer3 = a1;self.Answer4 = a1;
        answer = 'Answer'+str(odgovor)
        print(answer)

#Rasa Stojanovic
class QuestionForm(Form):
    Points = forms.IntegerField()
    Question = forms.CharField(max_length=50)
    Answer1 = forms.CharField(max_length=50)
    Answer2 = forms.CharField(max_length=50)
    Answer3 = forms.CharField(max_length=50)
    Answer4 = forms.CharField(max_length=50)
    #widget =  forms.RadioSelect(choices=TACNI_ODGOVORI)
    choice = forms.ChoiceField(widget=RadioSelect(), choices=[(1, 'Answer1'), (2, 'Answer2'),(3,'Answer3'),(4,'Answer4')])

class SearchCategoryForm(Form):
    filter = forms.CharField(max_length=50)

#Dejan Draskovic
#form for testing on article
class Testing(Form):
    question_text = ""
    def change(self ,q, a1, a2, a3, a4, name):
        self.fields[name] = forms.ChoiceField(widget=RadioSelect(), choices=[('1', a1), ('2', a2), ('3', a3), ('4', a4)])
        self.question_text = q

# Ilija Markovic i Marko Brkic
class createArticle(Form):
    title=forms.CharField(max_length=50,required=True)
    content = forms.CharField(widget=SummernoteWidget(),required=True)
    previewPic = forms.ImageField(required=False)
    #letters = forms.MultipleChoiceField()
    def f(self, kategorije):
        choices = list()

        for kat in kategorije:

            choices.append((kat.categoryId, kat.name))
            
        self.fields["letters"] = forms.MultipleChoiceField(choices=choices,label="",required=False,widget = forms.CheckboxSelectMultiple)

#Rasa Stojanovic
class updateArticle(Form):
    title = forms.CharField(max_length=50, required=True)
    content = forms.CharField(widget=SummernoteWidget(), required=True)
    previewPic = forms.ImageField(required=False)
    categories = forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple)
    # letters = forms.MultipleChoiceField()
    def __init__(self, *args,**kwargs):
        allCategories = [(cat.categoryId, cat.name) for cat in Category.objects.all()]
        sCategories=kwargs.pop('selectedCategories')
        super(updateArticle,self).__init__(*args,**kwargs)
        self.fields['categories'].choices = allCategories
        self.fields['categories'].initial = sCategories







