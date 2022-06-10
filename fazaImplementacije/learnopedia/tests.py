from django.test import TestCase
from .models import *
from django.contrib.auth.models import Group

from django.contrib import auth
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.

# fixtures


def create_category(name, desc):
    return Category.objects.create(name=name,description=desc)

def create_article(kor):
    return Article.objects.create(title="Test article", slug="test", isValidated=1,
    textContent="ovo je clanak", textContentRaw="ovo je clanak", korisnikId=kor)

def create_mod2(username):
    kor = Korisnik(username=username,isModerator=1)
    kor.set_password('Tash@1234')
    kor.save()
    return kor


def create_likedArticle(article,user):
    return KorisnikLikedArticle.objects.create(articleId=article, korisnikId=user)
    
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

def create_category(name, desc):
    return Category.objects.create(name=name,description=desc)

def create_ArticleCategory(article, category):
    return ArticleCategory.objects.create(articleId=article, categoryId=category)

def create_Comment(article, kor):
    return Comment.objects.create(articleId=article,korisnikId=kor,text='Ovo je Komentar')



#Rasa Stojanovic
class deleteComment(TestCase):
    def testDeleteComment(self):
        kor = create_mod('tasha')
        logged_in = self.client.login(username='tasha', password='T@sh@1234')

        article = create_article(kor)
        comm = create_Comment(article,kor)

        response1 =self.client.get("/deletecomment/" + str(comm.commentId))
        response2 = self.client.get("/article/" + str(article.articleId))
        self.assertNotContains(response2, "Ovo je Komentar")

#Rasa Stojanovic
class deleteCategory(TestCase):
    def testDeleteCategory(self):
        kor = create_mod('tasha')
        logged_in = self.client.login(username='tasha', password='T@sh@1234')

        article = create_article(kor)
        category = create_category("Fudbal","to je sport")
        article_category = create_ArticleCategory(article,category)

        response1 = self.client.get("/" + str(article.articleId) + "/deleteCategory/" + str(category.categoryId))
        response2 = self.client.get("/article/" + str(article.articleId))
        self.assertNotContains(response2, "Fudbal")

#Rasa Stojanovic
class ArticleTest(TestCase):
    def testArticleView(self):
        kor = create_mod("tasha")
        art = create_article(kor)
        url_pk = art.pk
        response = self.client.get("/article/" + str(url_pk))
        self.assertContains(response, "ovo je clanak")

#Rasa Stojanovic
class ProfileTest(TestCase):
    def testProfileView(self):
        kor = create_mod("tasha")
        url_pk = kor.pk
        response = self.client.get("/profile/" + str(url_pk))
        self.assertContains(response, "tasha")

#Rasa Stojanovic
class LoginTest(TestCase):
    def test_login(self):
        kor = create_mod2('test')
        url = "/login/"

        responseLogin = self.client.post(url, data={
            'username' : 'test',
            'password' : 'Tash@1234',
        })
        user = auth.get_user(self.client)
        print(user)
        response = self.client.get("")
        self.assertContains(response, "Logout")


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

#Marko Brkic
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

#Dejan Draskovic
class index_view_test(TestCase):
    def test_search(self):
        kor = create_mod('tasha')
        logged_in = self.client.login(username='tasha', password='T@sh@1234')
        clanak = create_article(kor)
        response = self.client.post("", data={
            "filter": "clanak",
            "validatedArticlesOnly": False,
        })
        self.assertContains(response, "ovo")


#Dejan Draskovic
class updateProfile_view_test(TestCase):
    def test_update_profile(self):
        kor = create_mod('tasha')
        logged_in = self.client.login(username='tasha', password='T@sh@1234')

        response1 = self.client.post("/updateProfile/"+str(kor.id), data={
            "username": "Dejan",
            "firstName": "Dejan",
            "lastName": "Draskovic",
            "description": "New description",
        })

        response2 = self.client.get("/profile/"+str(kor.id))
        self.assertContains(response2, "Draskovic")


#Dejan Draskovic
class categories_view_test(TestCase):
    def test_categories_filter(self):
        kor = create_mod('tasha')
        logged_in = self.client.login(username='tasha', password='T@sh@1234')
        category = create_category("testiranje", "sluzi za testiranje")
        article = create_article(kor)
        ac = create_ArticleCategory(article, category)

        response1 = self.client.post("/categories", data={
            "filter": "test"
        })
        self.assertContains(response1, "testiranje")

        response2 = self.client.get("/category/" + str(category.categoryId))
        self.assertContains(response2, "clanak")



#Dejan Draskovic
class kreiraj_article_view_test(TestCase):
    def test_create_article(self):
        kor = create_mod('tasha')
        logged_in = self.client.login(username='tasha', password='T@sh@1234')

        response1 = self.client.post("/create_article", data={
            "title": "New article",
            "content": "New content"
        })

        response2 = self.client.get("")
        self.assertContains(response2, "article")


#Dejan Draskovic
class deleteArticle_view_test(TestCase):
    def test_delete_article(self):
        kor = create_mod('tasha')
        logged_in = self.client.login(username='tasha', password='T@sh@1234')
        article = create_article(kor)

        response1 = self.client.get("/deleteArticle/"+str(article.articleId))
        response2 = self.client.get("")
        self.assertNotContains(response2, "clanak")

#Ilija Markovic
class category_test(TestCase):

    def test_category(self):
        category=create_category("family","family")
        url_name="/category/"+str(category.categoryId)
        response=self.client.get(url_name)
        self.assertContains(response,"family")




#Ilija Markovic
class likeArticle_test(TestCase):

    def test_likeArticle(self):
        kor = create_mod('tasha')
        logged_in = self.client.login(username='tasha', password='T@sh@1234')
        clanak = create_article(kor)
        KorisnikLikedArticle=create_likedArticle(clanak,kor)
        urlLikeArticle = "/article/" + str(clanak.articleId)

        responseArticle = self.client.get(urlLikeArticle)
        self.assertContains(responseArticle, '1')

#Ilija Markovic
class validateArticle_test(TestCase):

    def test_validateArticle(self):
        kor = create_mod('tasha')
        logged_in = self.client.login(username='tasha', password='T@sh@1234')
        clanak = create_article(kor)
        urlValidateArticle = "/article/" + str(clanak.articleId)

        responseArticle = self.client.get(urlValidateArticle)
        self.assertNotContains(responseArticle,'Approve article')

#Ilija Markovic
class createCategory_test(TestCase):

    def test_createCategor(self):
        kor = create_mod('tasha')
        logged_in = self.client.login(username='tasha', password='T@sh@1234')

        urlcreateCategor = "/create_category/"

        responseTest = self.client.post(urlcreateCategor, data={
            'name': 'sport',
            'description':'sport'
        })

        response=self.client.get("/categories")
        self.assertContains(response, 'sport')

#Ilija Markovic
class updateArticle_test(TestCase):

    def test_updateArticle(self):
        kor = create_mod('tasha')
        logged_in = self.client.login(username='tasha', password='T@sh@1234')
        clanak = create_article(kor)
        urlUpdate="/articleUpdate/"+str(clanak.articleId)


        responseTest = self.client.post(urlUpdate, data={
            'title': 'Test article 1',
            'content': 'ovo je clanak 1',

        })

        response = self.client.get("")
        self.assertContains(response, 'ovo je clanak 1')

#Ilija Markovic
class banUser_test(TestCase):

    def test_banUser(self):
        kor = create_mod('tasha')
        clanak = create_article(kor)

        kor2 = create_mod2('tasha2')
        logged_in = self.client.login(username='tasha2', password='Tash@1234')

        banUrl="/ban/"+str(kor.id)
        response = self.client.get(banUrl)

        response = self.client.get("")
        self.assertNotContains(response, 'Test article')










