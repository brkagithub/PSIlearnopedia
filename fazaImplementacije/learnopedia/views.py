from django.shortcuts import render

# Create your views here.

from django.http import HttpRequest
from .models import *

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

def profile(request: HttpRequest, profile_id):
    return render(request, 'profile.html')

def categories(request: HttpRequest):
    return render(request, 'categories.html')