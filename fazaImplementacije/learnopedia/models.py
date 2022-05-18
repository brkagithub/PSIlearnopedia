from django.db import models

# Create your models here

from django.contrib.auth.models import AbstractUser, User
import datetime

class Korisnik(AbstractUser):
    isModerator = models.IntegerField(db_column='isModerator', default=False)  # Field name made lowercase.
    isAdministrator = models.IntegerField(db_column='isAdministrator', default=False)  # Field name made lowercase.
    profilePic = models.TextField(db_column='profilePic', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Korisnik'

class Article(models.Model):
    articleId = models.AutoField(db_column='articleId', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=25)
    slug = models.CharField(unique=True, max_length=25)
    createdAt = models.DateTimeField(default=datetime.datetime.now())
    isValidated = models.IntegerField(db_column='isValidated')  # Field name made lowercase.
    textContent = models.TextField(db_column='textContent')  # Field name made lowercase.
    previewPicture = models.TextField(db_column='previewPicture', blank=True, null=True)  # Field name made lowercase.
    korisnikId = models.ForeignKey('Korisnik', models.DO_NOTHING, db_column='korisnikId')  # Field name made lowercase.

    class Meta:
        db_table = 'Article'


class ArticleCategory(models.Model):
    articleId = models.OneToOneField(Article, models.DO_NOTHING, db_column='articleId', primary_key=True)  # Field name made lowercase.
    categoryId = models.ForeignKey('Category', models.DO_NOTHING, db_column='categoryId')  # Field name made lowercase.

    class Meta:
        db_table = 'ArticleCategory'
        unique_together = (('articleId', 'categoryId'),)


class Category(models.Model):
    categoryId = models.AutoField(db_column='categoryId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=25)
    description = models.TextField()

    class Meta:
        db_table = 'Category'


class Comment(models.Model):
    commentId = models.AutoField(db_column='commentId', primary_key=True)  # Field name made lowercase.
    text = models.TextField()
    createdAt = models.DateTimeField(default=datetime.datetime.now())
    articleId = models.ForeignKey(Article, models.DO_NOTHING, db_column='articleId')  # Field name made lowercase.
    korisnikId = models.ForeignKey('Korisnik', models.DO_NOTHING, db_column='korisnikId')  # Field name made lowercase.

    class Meta:
        db_table = 'Comment'


class Question(models.Model):
    questionId = models.AutoField(db_column='questionId', primary_key=True)  # Field name made lowercase.
    text = models.TextField()
    answer1 = models.CharField(max_length=50, blank=True, null=True)
    answer2 = models.CharField(max_length=50, blank=True, null=True)
    answer3 = models.CharField(max_length=50, blank=True, null=True)
    answer4 = models.CharField(max_length=50, blank=True, null=True)
    points = models.IntegerField()
    correct = models.IntegerField()
    articleId = models.ForeignKey(Article, models.DO_NOTHING, db_column='articleId')  # Field name made lowercase.

    class Meta:
        db_table = 'Question'

class KorisnikArticleGrade(models.Model):
    articleId = models.ForeignKey(Article, models.DO_NOTHING, db_column='articleId')  # Field name made lowercase.
    korisnikId = models.ForeignKey(Korisnik, models.DO_NOTHING, db_column='korisnikId')  # Field name made lowercase.
    grade = models.IntegerField()

    class Meta:
        db_table = 'KorisnikArticleGrade'
        unique_together = (('articleId', 'korisnikId'),)


class KorisnikLikedArticle(models.Model):
    korisnikId = models.ForeignKey(Korisnik, models.DO_NOTHING, db_column='korisnikId')  # Field name made lowercase.
    articleId = models.ForeignKey(Article, models.DO_NOTHING, db_column='articleId')  # Field name made lowercase.

    class Meta:
        db_table = 'KorisnikLikedArticle'
        unique_together = (('korisnikId', 'articleId'),)