from django.contrib import admin

from .models import *

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('textContent',)


admin.site.register(Article, PostAdmin)
admin.site.register(Korisnik)
#admin.site.register(Article)
admin.site.register(ArticleCategory)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Question)
admin.site.register(KorisnikArticleGrade)
admin.site.register(KorisnikLikedArticle)