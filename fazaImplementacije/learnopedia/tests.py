from django.test import TestCase
from .models import *
from django.contrib.auth.models import Group
from django.contrib import auth
from django.core.files.uploadedfile import SimpleUploadedFile
# Create your tests here.

# fixtures

def create_mod(username):
    kor = Korisnik(username=username)
    kor.set_password('T@sh@1234')
    Group.objects.create(name='mod')
    group = Group.objects.get(name='mod')
    kor.save()
    kor.groups.add(group)
    return kor

def create_article(kor):
    return Article.objects.create(title="Test article", slug="test", isValidated=1,
    textContent="ovo je clanak", textContentRaw="ovo je clanak", korisnikId=kor)

def create_question(kor, choice, answer1, answer2,
                    answer3, answer4, article, textquestion, points):
    return Question(correct=choice,answer1=answer1,answer2=answer2,
       answer3=answer3,answer4=answer4,articleId=article,text=textquestion,points=points)

# Marko Brkic
class MakeCommentTest(TestCase):
    def test_makecomment(self):
        kor = create_mod('tasha')
        logged_in = self.client.login(username='tasha', password='T@sh@1234')
        clanak = create_article(kor)
        #makecomment(kor, 'Volim ovaj clanak!', clanak)
        urlArticle = "/article/" + str(clanak.articleId)
        urlMakeComment = "/makecomment/" + str(clanak.articleId)

        responseMakeComment = self.client.post(urlMakeComment, data={
            'text' : 'Volim ovaj clanak!'
        })

        #print(url)
        responseArticle = self.client.get(urlArticle)
        self.assertContains(responseArticle, 'Volim ovaj clanak!')

# Marko Brkic
class RegistrationTest(TestCase):
    def test_register(self):
        url = "/register/"

        responseRegister = self.client.post(url, data={
            'username' : 'tester',
            'password1' : 'cokoladica134',
            'password2': 'cokoladica134',
            'first_name' : 'testivoje',
            'last_name' : 'testirovic',
            'description' : 'im a tester',
        })

        user = auth.get_user(self.client)
        print(user)
        assert user.is_authenticated

# Marko Brkic
class MakeQuestionTest(TestCase):
    def test_makequestion(self):
        kor = create_mod('tasha')
        logged_in = self.client.login(username='tasha', password='T@sh@1234')
        clanak = create_article(kor)

        urlTest = "/test/" + str(clanak.articleId)
        urlMakeQuestion = "/makequestions/" + str(clanak.articleId)

        responseMakeQuestion = self.client.post(urlMakeQuestion, data={
            'Question': 'Koliko je 2+2',
            'Answer1': '3',
            'Answer2': '4',
            'Answer3': '5',
            'Answer4': '6',
            'choice': "2",
            'Points' : 5
        })

        responseTest = self.client.get(urlTest)
        self.assertContains(responseTest, 'Koliko je 2+2')

# Marko Brkic
class TestingTest(TestCase):
    def test_testing(self):
        kor = create_mod('tasha')
        logged_in = self.client.login(username='tasha', password='T@sh@1234')
        clanak = create_article(kor)
        clanak.save()
        question1 = create_question(kor, 2, "3", "4", "5", "6", clanak, "Koliko je 2+2", 5)
        question2 = create_question(kor, 4, "3", "4", "5", "6", clanak, "Koliko je 3+3", 5)
        question1.save()
        question2.save()

        #print(clanak.articleId)

        urlTest = "/test/" + str(clanak.articleId)

        responseTest = self.client.post(urlTest, data={
            'q0' : 2,
            'q1' : 2
        })

        self.assertContains(responseTest, 'mali ste 50')

class UpdateQuestionsTest(TestCase):
    def test_UpdateQuestions(self):
        kor = create_mod('tasha')
        logged_in = self.client.login(username='tasha', password='T@sh@1234')
        clanak = create_article(kor)
        clanak.save()
        question1 = create_question(kor, 2, "3", "4", "5", "6", clanak, "Koliko je 2+2", 5)
        question2 = create_question(kor, 4, "3", "4", "5", "6", clanak, "Koliko je 3+3", 5)
        question1.save()
        question2.save()

        urlUpdate = "/questionUpdate/" + str(clanak.articleId)

        responseTest1 = self.client.post(urlUpdate, data={
            'Question': 'Koliko je 2+3',
            'Answer1': '3',
            'Answer2': '4',
            'Answer3': '5',
            'Answer4': '6',
            'choice': "3",
            'Points' : 5
        })

        responseTest2 = self.client.post(urlUpdate, data={
            'Question': 'Koliko je 4+3',
            'Answer1': '3',
            'Answer2': '4',
            'Answer3': '5',
            'Answer4': '7',
            'choice': "4",
            'Points': 5
        })

        urlTest = "/test/" + str(clanak.articleId)

        responseTest = self.client.get(urlTest)
        self.assertContains(responseTest, 'Koliko je 4+3')
        self.assertContains(responseTest, 'Koliko je 2+3')