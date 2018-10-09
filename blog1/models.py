from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Comment(models.Model):
    pub_time = models.DateTimeField('评论发表时间', auto_now=True)
    content = models.TextField('评论内容', null=False, default='no comment')
    name = models.CharField('评论者名字', max_length=10, null=False)
    url = models.URLField(max_length=20, null=False)
    email = models.EmailField('评论者邮箱', max_length=20, null=False)
    article = models.ForeignKey('Article', verbose_name='评论所属文章', on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:20]


class Article(models.Model):
    title = models.CharField(max_length=70, null=False)
    content = models.TextField()
    create_time = models.DateTimeField()
    modifies_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title
