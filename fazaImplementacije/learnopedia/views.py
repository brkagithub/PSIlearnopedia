from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from .forms import *
# Create your views here.

from django.http import HttpRequest
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def index(request: HttpRequest):
    return render(request, 'home.html')

def article(request: HttpRequest, article_id):
    article = Article.objects.get(pk=article_id)

    articlesFromAuthor = Article.objects.filter(korisnikId__exact=article.korisnikId)

    totalLikes = 0

    for a in articlesFromAuthor:
        totalLikes += KorisnikLikedArticle.objects.filter(articleId__exact=a.articleId).count()


    context = {"article" : article, "totalLikes": totalLikes}

    return render(request, 'article.html', context)

@login_required(login_url='login')
def profile(request: HttpRequest, profile_id):
    return render(request, 'profile.html')

def categories(request: HttpRequest):
    return render(request, 'categories.html')

def login_req(request: HttpRequest):
    form = AuthenticationForm(request=request, data=request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            print("Successful login")
            return redirect('home')
    else:
        print("Unuccessful login")

    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def logout_req(request: HttpRequest):
    logout(request)
    return redirect('home')

def registration(request: HttpRequest):
    form = KorisnikCreationForm(request.POST, request.FILES)
    if form.is_valid():
        user:Korisnik = form.save()
        login(request, user)
        return redirect('home')
    else:
        for field in form:
            print("Field Error:", field.name, field.errors)

    context = {
        'form': form
    }
    return render(request, 'register.html', context)
