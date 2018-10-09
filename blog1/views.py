from django.shortcuts import render
from . import models
import datetime
# Create your views here.


def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog1/index.html', {'articles': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog1/article_page.html', {'article': article})


def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog1/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog1/edit_page.html', {'article': article})


def edit_action(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article_id = request.POST.get('article_id', '0')
    if str(article_id) == '0':
        if title == '':
            articles = models.Article.objects.all()
            return render(request, 'blog1/index.html', {'articles': articles})
        else:
            models.Article.objects.create(title=title, content=content)
            articles = models.Article.objects.all()
            return render(request, 'blog1/index.html', {'articles': articles})
    else:
        article = models.Article.objects.get(pk=article_id)
        article.title = title
        article.body = content
        article.create_time = datetime.date
        article.save()
        return render(request, 'blog1/article_page.html', {'article': article})