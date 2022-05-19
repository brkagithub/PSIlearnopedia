from django.shortcuts import render

# Create your views here.

from django.http import HttpRequest
from .models import *
from django.db.models import Q

def index(request: HttpRequest):
    return render(request, 'home.html')

def article(request: HttpRequest, article_id):
    article = Article.objects.get(pk=article_id)

    articlesFromAuthor = Article.objects.filter(korisnikId__exact=article.korisnikId)

    totalLikes = 0

    for a in articlesFromAuthor:
        totalLikes += KorisnikLikedArticle.objects.filter(articleId__exact=a.articleId).count()

    categories = ArticleCategory.objects.filter(articleId__exact=article_id)

    categoriesToShow = []

    for category in categories:
        categoriesToShow.append(category.categoryId)

    threeArticles = articlesFromAuthor.filter(~Q(articleId__exact=article_id))[:3] # We should make a numOfLikes field in Article to make this easier

    context = {"article" : article, "totalLikes": totalLikes, "categoriesToShow" : categoriesToShow, "threeArticles" : threeArticles}

    return render(request, 'article.html', context)

def profile(request: HttpRequest, profile_id):
    return render(request, 'profile.html')

def category(request: HttpRequest, category_id):
    return render(request, 'home.html')

def categories(request: HttpRequest):
    return render(request, 'categories.html')