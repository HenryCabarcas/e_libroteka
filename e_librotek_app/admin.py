from django.contrib import admin
from .models import Book
from .models import Comment
from .models import User

admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(User)
