from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Korisnik)
admin.site.register(Article)
admin.site.register(ArticleCategory)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Question)
admin.site.register(KorisnikArticleGrade)
admin.site.register(KorisnikLikedArticle)