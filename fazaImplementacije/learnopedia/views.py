
# Create your views here.

import json

from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.http import HttpRequest
from .models import *
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, permission_required


def index(request: HttpRequest):
        searchform = SearchForm(request.POST or None)
        articles = []
        if searchform.is_valid():
            term = searchform.cleaned_data["filter"]
            articles = Article.objects.filter(Q(textContent__contains=term) | Q(title__contains=term) | Q(korisnikId__username__contains=term) )
        else:
            category_id = request.POST.get('category_id')
            if category_id :
                ArticlesWithCategory = ArticleCategory.objects.filter(categoryId = category_id)
                for ArticleWithCategory in ArticlesWithCategory:
                    articles.append(ArticleWithCategory.articleId)
            else:
                articles = Article.objects.order_by('-title')
        searchform = SearchForm()
        context = {
            'searchform': searchform,
            'articles':articles
        }
        return render(request, 'home.html', context)

def category(request: HttpRequest, category_id):
    articles = []
    ArticlesWithCategory = ArticleCategory.objects.filter(categoryId=category_id)
    for ArticleWithCategory in ArticlesWithCategory:
        articles.append(ArticleWithCategory.articleId)
    searchform = SearchForm()
    context = {
        'searchform': searchform,
        'articles': articles
    }
    return render(request, 'home.html',context)


cnt=0
@login_required(login_url='login')
def UpdateQuestions(request:HttpRequest, article_id):
    korisnik_current = request.user
    article = Article.objects.get(articleId=article_id)
    owner = Korisnik.objects.get(pk=article.korisnikId.pk)
    if (
            owner.pk != korisnik_current.pk and korisnik_current.isModerator == 0 and korisnik_current.isAdministrator == 0):
        return redirect('home')
    updateform = QuestionUpdateForm(request.POST or None)
    global cnt
    if( request.method == 'GET'):
        cnt = 0
    if( request.method == 'POST'):

        if updateform.is_valid():
            textquestion = updateform.cleaned_data['Question']
            answer1 = updateform.cleaned_data['Answer1']
            answer2 = updateform.cleaned_data['Answer2']
            answer3 = updateform.cleaned_data['Answer3']
            answer4 = updateform.cleaned_data['Answer4']
            choice = int(updateform.cleaned_data['choice'])
            points = updateform.cleaned_data['Points']
            article = Article.objects.get(articleId=article_id)
            question = Question.objects.filter(articleId=article_id)[cnt]
            question.answer1 = answer1; question.answer3 = answer3
            question.answer2 = answer2; question.answer4 = answer4
            question.text= textquestion; question.correct = choice
            question.points=points
            question.save()
            cnt = cnt + 1

    if(Question.objects.filter(articleId=article_id).count() > cnt):
        question = Question.objects.filter(articleId=article_id)[cnt]
        a1 = question.answer1; a2 = question.answer2; a3 = question.answer3; a4 = question.answer4;
        q = question.text;  odgovor = question.correct; points = question.points
        updateform = QuestionUpdateForm(initial= {'Question':q,'Answer1':a1,'Answer2':a2,'Answer3':a3,'Answer4':a4,'choice': odgovor, 'points':points})
    else:
        updateform = QuestionUpdateForm()
    context = {
        'updateForm': updateform,
    }
    return render(request, 'questionUpdate.html', context)



@login_required(login_url='login')
def makequestions(request: HttpRequest, article_id):
    questionform = QuestionForm(request.POST or None)
    if(questionform.is_valid()):
        textquestion = questionform.cleaned_data['Question']
        answer1 = questionform.cleaned_data['Answer1']
        answer2 = questionform.cleaned_data['Answer2']
        answer3 = questionform.cleaned_data['Answer3']
        answer4 = questionform.cleaned_data['Answer4']
        points  = questionform.cleaned_data['Points']
        choice = int(questionform.cleaned_data['choice'])
        article= Article.objects.get(articleId=article_id)
        question = Question(correct=choice,answer1=answer1,answer2=answer2,answer3=answer3,answer4=answer4,articleId=article,text=textquestion,points=points)
        question.save()
        questionform = QuestionForm()

        button = request.POST.get("makequestion")
        if button == 'Finish':                          #if finished making questions go to article
            return redirect('article', article_id)


    context ={
        'questionform' : questionform,
        'articleId' : article_id
    }
    return render(request, 'makequestions.html', context)


def article(request: HttpRequest, article_id): #view for viewing an article
    article = Article.objects.get(pk=article_id)
    comments = Comment.objects.filter(articleId__exact=article)     #getting all comments for article
    korisnik = request.user

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

    context = {"article" : article, "totalLikes": totalLikes, "categoriesToShow" : categoriesToShow, "threeArticles" : threeArticles, "userLiked" : userLiked, "comments": comments, "korisnik":korisnik}

    return render(request, 'article.html', context)

@login_required(login_url='login')
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



def categories(request: HttpRequest):
    searchcategory = SearchCategoryForm(request.POST or None)
    if searchcategory.is_valid():
        term = searchcategory.cleaned_data['filter']
        categories = Category.objects.filter(Q(name__contains = term) | Q(description__contains = term))
    else:
        categories = Category.objects.all()
    context = {
        'categories' : categories,
        'searchCategory' : searchcategory,
            }
    return render(request, 'categories.html', context)


def login_req(request: HttpRequest):    #login korisnik
    form = AuthenticationForm(request=request, data=request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)    #autorization korisnik

        if user:
            login(request, user)         #successful login
            return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def logout_req(request: HttpRequest):        #logout korisnik
    logout(request)
    return redirect('home')

def registration(request: HttpRequest):       #register korisnik
    form = KorisnikCreationForm(request.POST, request.FILES)
    if form.is_valid():
        user:Korisnik = form.save()          #adding korisnik to database
        login(request, user)                 #login newest korisnik
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


@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def validateArticle(request: HttpRequest, article_id): #view for approving an article by a moderator
    article = Article.objects.get(pk=article_id)
    article.isValidated=1
    article.save()
    return redirect('article', article_id)

@login_required(login_url='login')
def deleteCategory(request: HttpRequest, article_id, category_id): #view for deleting a category from an article
    article = Article.objects.get(pk=article_id)
    category = Category.objects.get(pk=category_id)
    articleCategory = ArticleCategory.objects.filter(articleId__exact=article).filter(categoryId__exact=category)
    articleCategory.delete()
    return redirect('article', article_id)

@login_required(login_url='login')
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

@login_required(login_url='login')
def test(request: HttpRequest, article_id):     #testiranje na pitanjima za clanak
    article = Article.objects.get(pk=article_id)
    korisnik = Korisnik.objects.get(pk=request.user.id)
    forms_questions = []               #forma za svako pitanje
    questions = Question.objects.filter(Q(articleId__exact=article_id))   #sva pitanja za izabrani clanak
    for count, question in enumerate(questions):                 #formiranje svih formi pitanja
        forms_questions.append(Testing(request.POST or None))
        forms_questions[count].change(question.text, question.answer1, question.answer2, question.answer3, question.answer4, "q"+str(count))

    valid_forms = True
    for form in forms_questions:     #provera da li su sve forme validne
        if form.is_valid():
            continue
        valid_forms = False
        break

    points = 0
    all_points = 0
    if valid_forms:
        if request.method == 'POST':
            for count, question in enumerate(questions):   #racunanje broja osvojenih poena
                choice = int(forms_questions[count].cleaned_data["q"+str(count)])
                if question.correct == choice:             #ako je tacan odgovor dodavanje poena
                    points += question.points
                all_points += question.points
            grade = points * 100 / all_points
            oldGrade = KorisnikArticleGrade.objects.filter(articleId__exact=article, korisnikId__exact=korisnik)
            if oldGrade:
                oldGrade.delete()                   #brisanje stare ocene na artiklu ako se korisnik vec testirao
            newGrade = KorisnikArticleGrade.objects.create(articleId=article, korisnikId=korisnik, grade=grade)    #upisivanje ocene korisnika na artiklu
            newGrade.save()

            context = {
                'grade': grade,
                'article_title': article.title,
                'article_id': article_id,
            }
            return render(request, 'results.html', context)

    context = {
        'forms_questions': forms_questions,
        'article_id':article_id,
    }
    return render(request, 'test.html', context)


@login_required(login_url='login')
def makecomment(request: HttpRequest, article_id):
    comment_form = CommentForm(request.POST or None)        #creating form to write comment

    if comment_form.is_valid():
        text = comment_form.cleaned_data['text']             #getting text of the comment
        article = Article.objects.get(pk=article_id)
        korisnik = request.user
        newComment = Comment.objects.create(articleId=article, korisnikId=korisnik, text=text)
        newComment.save()                   #saving  comment

        return redirect('article', article_id)

    context = {
        "comment_form": comment_form,
        "article_id": article_id
    }
    return render(request, 'makecomment.html', context)


@login_required(login_url='login')        #used for deleting comment
def comment(request: HttpRequest, comment_id):
    comment = Comment.objects.get(pk=comment_id)            #finding comment for deleting
    article = Article.objects.get(pk=comment.articleId.articleId)           #finding article to redirect to
    comment.delete()
    return redirect('article', article.articleId)


@csrf_exempt
@login_required(login_url='login')
def kreiraj_article(request: HttpRequest):
    flag = 0
    title = request.POST.get('naslov')
    kategorije1 = request.POST.getlist('kategorije[]')
    text = request.POST.get('tekst_artikla')
    flag = request.POST.get('flag')
    add_questions = request.POST.get('add_questions')
    kategorije = Category.objects.all()

    last_id = 0
    articles = Article.objects.all()
    if articles:

        last_article = Article.objects.all().last()
        last_id = last_article.articleId + 1

    else:
        last_id = 1

    username = None
    if request.user.is_authenticated:
        username = request.user.username
    current_user = request.user
    if flag:
        clanak = Article.objects.create(title=title, slug=text, isValidated=0, textContent=text, previewPicture="",
                                        korisnikId=current_user)
        for kat in kategorije1:
            kategorijap = Category.objects.filter(Q(name__exact=kat))
            kategorija = kategorijap[0]
            clanakKategorija = ArticleCategory.objects.create(articleId=clanak, categoryId=kategorija)
            clanakKategorija.save()
        clanak.save()

    context = {
        'kategorije': kategorije,
        'last_id': last_id,
        'flag': add_questions

    }

    return render(request, 'create_article.html', context)


