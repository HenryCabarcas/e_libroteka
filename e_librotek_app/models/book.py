from django.db import models
import datetime


class Book(models.Model):
    ISBN = models.CharField('ISBN', max_length=20,
                            unique=True, primary_key=True)
    title = models.CharField('title', max_length=50)
    author = models.CharField('author', max_length=128,
                              default="Anonymous", null=True)
    gender = models.CharField('gender', max_length=40, null=True)
    publicationDate = models.CharField(
        'publicationDate', max_length=4, null=True)
    formato = models.CharField(
        'formato', max_length=20, null=True, default='pdf')
    resume = models.TextField('resume', null=True)
    url = models.CharField('url', max_length=512, null=True)
    creationDate = models.DateTimeField(default=datetime.datetime.now())
    modificationDate = models.DateTimeField(default=datetime.datetime.now())
    pages = models.BigIntegerField(
        'pages', max_length=2000, default=0, null=True)
