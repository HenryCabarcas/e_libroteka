from e_librotek_app.models import Book, Comment
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['ISBN', 'title', 'author', 'url',
                  'gender', 'publicationDate', 'formato', 'resume', 'creationDate', 'modificationDate', 'pages']

    def to_representation(self, obj):
        book = Book.objects.get(ISBN=obj.ISBN)
        comments = list(Comment.objects.filter(book=obj.ISBN))
        print(comments)
        return {
            "ISBN": book.ISBN,
            "title": book.title,
            "author": book.author,
            "gender": book.gender,
            "publicationDate": book.publicationDate,
            "format": book.formato,
            "resume": book.resume,
            "url": book.url,
            "pages": book.pages,
            "comments": [
                {
                    "id": item.id,
                    "score": item.score,
                    "comment": item.comment,
                    "creationDate": item.creationDate,
                    "modificationDate": item.modificationDate
                }
                for item in comments
            ],
            "creationDate": book.creationDate,
            "modificationDate": book.modificationDate
        }
