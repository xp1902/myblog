from django.contrib import admin

from .models import Article
from .models import Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'create_time', 'modifies_time', 'author')
    list_filter = ('create_time', )

admin.site.register(Article, ArticleAdmin)