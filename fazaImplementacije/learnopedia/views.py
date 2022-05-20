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
        if (term == ''):
            articles = Article.objects.order_by('-title')
        else:
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
        questionform = QuestionForm()
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



def category(request: HttpRequest, category_id):
    return render(request, 'home.html')

def categories(request: HttpRequest):
    categories = Category.objects.all()
    context = {"categories" : categories}
    return render(request, 'categories.html', context)


def login_req(request: HttpRequest):    #login korisnika
    form = AuthenticationForm(request=request, data=request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)    #autorizacija korisnika

        if user:
            login(request, user)         #uspesno logovanje
            return redirect('home')
    else:
        print("Unuccessful login")      #neuspesno logovanje

    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def logout_req(request: HttpRequest):        #logout korisnika
    logout(request)
    return redirect('home')

def registration(request: HttpRequest):       #registracija korisnika
    form = KorisnikCreationForm(request.POST, request.FILES)
    if form.is_valid():
        user:Korisnik = form.save()          #belezenje u bazu korisnika
        login(request, user)                 #logovanje novonapravljenog korisnika
        return redirect('home')
    else:
        for field in form:
            print("Field Error:", field.name, field.errors)

    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def returnCategory(articleCategory: ArticleCategory): #helper function to return catId from ArticleCategory class
    return articleCategory.categoryId

def profile(request: HttpRequest, profile_id): #view for profile - shows basic info, most popular articles and grades by categories
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
def ban(request: HttpRequest, profile_id): #view for banning a user - deletes everything the user ever made (USE WITH CAUTION)
    user = Korisnik.objects.get(pk=profile_id) #delete everything related to this user

    for article in Article.objects.filter(korisnikId__exact=profile_id):
        for articleCategory in ArticleCategory.objects.filter(articleId__exact=article):
            articleCategory.delete()
        for articleGrade in KorisnikArticleGrade.objects.filter(Q(articleId__exact=article)  | Q(korisnikId__exact=profile_id)):
            articleGrade.delete()
        for articleLike in KorisnikLikedArticle.objects.filter(Q(articleId__exact=article)  | Q(korisnikId__exact=profile_id)):
            articleLike.delete()
        for question in Question.objects.filter(articleId__exact=article):
            question.delete()
        for comment in Comment.objects.filter(articleId__exact=article):
            comment.delete()
        article.delete()

    user.delete()
    return redirect('home')

def deleteArticle(request: HttpRequest, article_id): #view for deleting an article - deletes everything related to it too
    article = Article.objects.get(pk=article_id)
    for articleCategory in ArticleCategory.objects.filter(articleId__exact=article):
        articleCategory.delete()
    for articleGrade in KorisnikArticleGrade.objects.filter(articleId__exact=article):
        articleGrade.delete()
    for articleLike in KorisnikLikedArticle.objects.filter(articleId__exact=article):
        articleLike.delete()
    for question in Question.objects.filter(articleId__exact=article):
        question.delete()
    for comment in Comment.objects.filter(articleId__exact=article):
        comment.delete()
    article.delete()
    return redirect('home')

def validateArticle(request: HttpRequest, article_id): #view for approving an article by a moderator
    article = Article.objects.get(pk=article_id)
    article.isValidated=1
    article.save()
    return redirect('article', article_id)

def deleteCategory(request: HttpRequest, article_id, category_id): #view for deleting a category from an article
    article = Article.objects.get(pk=article_id)
    category = Category.objects.get(pk=category_id)
    articleCategory = ArticleCategory.objects.filter(articleId__exact=article).filter(categoryId__exact=category)
    articleCategory.delete()
    return redirect('article', article_id)

def updateProfile(request: HttpRequest, profile_id): #view for updating a user's profile
    profile = Korisnik.objects.get(pk=profile_id)

    updateForm = UpdateUserForm(request.POST or None)

    if updateForm.is_valid():
        print("valid")
        profile.username = updateForm.cleaned_data["username"]
        profile.first_name = updateForm.cleaned_data["firstName"]
        profile.last_name = updateForm.cleaned_data["lastName"]
        profile.description = updateForm.cleaned_data["description"]
        profile.save()
        return redirect("profile", profile.id)

    context = {"profile" : profile, "form": updateForm }
    return render(request, 'updateProfile.html', context)

def test(request: HttpRequest, article_id):     #testiranje na pitanjima za clanak

    forms_questions = []               #forma za svako pitanje
    answers_questions = []             #lista liste odgovora za svako pitanje
    iterator = []
    article = Article.objects.get(pk=article_id)
    questions = Question.objects.filter(Q(articleId__exact=article_id))   #sva pitanja za izabrani clanak
    for index in range(len(questions)):
        forms_questions.append(Testiranje(request.POST or None))     #pravljenje forme za svako pitanje
        answer1 = questions[index].answer1
        answer2 = questions[index].answer2
        answer3 = questions[index].answer3
        answer4 = questions[index].answer4
        answers_questions.append([answer1, answer2, answer3, answer4])
        iterator.append(index)


    context = {
        'questions': questions,
        'answers_questions': answers_questions,
        'forms_questions': forms_questions,
        'iterator': iterator
    }
    return render(request, 'questions.html', context)


