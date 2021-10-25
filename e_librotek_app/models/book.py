from django.db import models
import datetime


class Book(models.Model):
    ISBN = models.CharField('ISBN', max_length=20,
                            unique=True, primary_key=True)
    title = models.CharField('title', max_length=50)
    volume = models.CharField('volume', max_length=50, default="1")
    gender = models.CharField('gender', max_length=40, null=True)
    editorial = models.CharField('editorial', max_length=80, null=True)
    formato = models.CharField(
        'formato', max_length=20, null=True, default='pdf')
    resume = models.TextField('resume', null=True)
    url = models.CharField('url', max_length=512, null=True)
    creationDate = models.DateTimeField(default=datetime.datetime.now())
    modificationDate = models.DateTimeField(default=datetime.datetime.now())
