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

def makequestions(request: HttpRequest, article_id):
    questionform = QuestionForm(request.POST or None)
    if( questionform.is_valid()):
        textquestion=questionform.cleaned_data['Question']
        answer1 = questionform.cleaned_data['Answer1']
        answer2 = questionform.cleaned_data['Answer2']
        answer3 = questionform.cleaned_data['Answer3']
        answer4 = questionform.cleaned_data['Answer4']
        choice = int(questionform.cleaned_data['choice'])
        article= Article.objects.get(articleId=article_id)
        question = Question(correct=choice,answer1=answer1,answer2=answer2,answer3=answer3,answer4=answer4,articleId=article,text=textquestion,points=0)
        question.save()
    context ={
        'questionform' : questionform,
    }
    return render(request, 'makequestions.html',context)


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


def profile(request: HttpRequest, profile_id):
    return render(request, 'profile.html')

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

