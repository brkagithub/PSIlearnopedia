"""fazaImplementacije URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', index, name="home"),
    path('article/<int:article_id>', article, name="article"),
    path('article/like/<int:article_id>', articleLike, name="articleLike"),
    path('profile/<int:profile_id>', profile, name="profile"),
    path('category/<int:category_id>', category, name="category"),
    path('categories', categories, name="categories"),
    path('login/', login_req, name='login'),
    path('logout/', logout_req, name='logout'),
    path('register/', registration, name='register'),
    path('create_article/', kreiraj_article, name='create_article'),
    path('ban/<int:profile_id>', ban, name='ban'),
    path('deleteArticle/<int:article_id>', deleteArticle, name='deleteArticle'),
    path('validateArticle/<int:article_id>', validateArticle, name='validateArticle'),
    path('<int:article_id>/deleteCategory/<int:category_id>', deleteCategory, name='deleteCategory'),
    path('updateProfile/<int:profile_id>', updateProfile, name="updateProfile"),
    path('makequestions/<int:article_id>',makequestions, name='makequestion'),
    path('test/<int:article_id>', test, name="test"),
    path('makecomment/<int:article_id>', makecomment, name='makecomment'),
    path('comment/<int:comment_id>', comment, name='comment'),
    path('questionUpdate/<int:article_id>', UpdateQuestions, name='questionUpdate'),
    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)