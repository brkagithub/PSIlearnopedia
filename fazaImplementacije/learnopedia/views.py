# Create your views here.

from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.http import HttpRequest
from .models import *
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

def index(request: HttpRequest):
    searchform = SearchForm(request.POST or None)
    articles = []
    if searchform.is_valid():
        term = searchform.cleaned_data["filter"]
        articles = Article.objects.filter(Q(textContent__contains=term) | Q(title__contains=term) | Q(korisnikId__username__contains=term) )
    else:
        articles = Article.objects.order_by('-title')
    context = {
        'searchform': searchform,
        'articles':articles
    }
    return render(request, 'home.html', context)

def article(request: HttpRequest, article_id): #view for viewing an article
    article = Article.objects.get(pk=article_id)

    articlesFromAuthor = Article.objects.filter(korisnikId__exact=article.korisnikId).order_by('-numOfLikes') #we sort it by likes

    totalLikes = 0

    for a in articlesFromAuthor:
        totalLikes += KorisnikLikedArticle.objects.filter(articleId__exact=a.articleId).count() #so we can show totalLikes

    categories = ArticleCategory.objects.filter(articleId__exact=article_id)

    categoriesToShow = [] #we show all categories of the article

    for category in categories:
        categoriesToShow.append(category.categoryId)

    #we show three of the most liked articles from the author too
    threeArticles = articlesFromAuthor.filter(~Q(articleId__exact=article_id))[:3] # sorted by likes already

    userLiked = False
    if request.user.is_authenticated:
        userLiked = KorisnikLikedArticle.objects.filter(korisnikId__exact=request.user).filter(articleId__exact=article_id).count() > 0

    context = {"article" : article, "totalLikes": totalLikes, "categoriesToShow" : categoriesToShow, "threeArticles" : threeArticles, "userLiked" : userLiked}

    return render(request, 'article.html', context)

def articleLike(request: HttpRequest, article_id): #view for liking an article
    article = Article.objects.get(pk=article_id)
    if(KorisnikLikedArticle.objects.filter(articleId__exact=article_id).filter(korisnikId__exact=request.user.id).count() == 0): #if he liked
        newLike = KorisnikLikedArticle.objects.create(articleId=article, korisnikId=request.user)
        newLike.save()
        article.numOfLikes+=1
        article.save()
    else:
        KorisnikLikedArticle.objects.filter(articleId__exact=article_id).filter(korisnikId__exact=request.user.id).delete()
        article.numOfLikes -= 1
        article.save()
    return redirect('article', article_id)


def returnCategory(articleCategory: ArticleCategory):
    return articleCategory.categoryId

def profile(request: HttpRequest, profile_id):
    profile = Korisnik.objects.get(pk=profile_id)

    top5Articles = Article.objects.filter(korisnikId__exact=profile_id).order_by('-numOfLikes')[:5]

    userGrades = KorisnikArticleGrade.objects.filter(korisnikId__exact=profile_id)

    readArticleCategories = {}

    for userGrade in userGrades: # finding top 5 categories the user did tests
        article = userGrade.articleId # we pass numbers of articles from that category and the average score
        grade = userGrade.grade
        articleCategories = ArticleCategory.objects.filter(articleId__exact=article)
        categories = map(returnCategory, articleCategories)

        for category in categories:
            if category.name not in readArticleCategories:
                readArticleCategories[category.name] = (1, grade)
            else:
                newCount = readArticleCategories[category.name][0] + 1
                totalGrade = readArticleCategories[category.name][1] + grade

                readArticleCategories[category.name] = (newCount, totalGrade)

    top5Categories = []

    for categoryAndNum in sorted(readArticleCategories.items(), key=lambda x: x[1][0], reverse=True)[:5]:
            top5Categories.append((categoryAndNum[0], (categoryAndNum[1][0], round(categoryAndNum[1][1] / categoryAndNum[1][0], 2))))

    context = {"profile" : profile, "top5Articles" : top5Articles, "top5Categories" : top5Categories}
    return render(request, 'profile.html', context)

def category(request: HttpRequest, category_id):
    return render(request, 'home.html')

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