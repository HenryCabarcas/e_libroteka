from django.db import models
from .book import Book
import datetime


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, related_name="book",
                             on_delete=models.CASCADE)
    score = models.IntegerField('score', default=3)
    comment = models.CharField('comment', max_length=500)
    creationDate = models.DateTimeField(default=datetime.datetime.now())
    modificationDate = models.DateTimeField(default=datetime.datetime.now())
