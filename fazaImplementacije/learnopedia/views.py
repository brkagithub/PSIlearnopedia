from django.shortcuts import render

# Create your views here.

from django.http import HttpRequest

def index(request: HttpRequest):
    return render(request, 'home.html')

def article(request: HttpRequest, article_id):
    return render(request, 'article.html')

def profile(request: HttpRequest, profile_id):
    return render(request, 'profile.html')

def categories(request: HttpRequest):
    return render(request, 'categories.html')