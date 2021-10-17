from e_librotek_app.models import Book, Comment
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['ISBN', 'title', 'volume',
                  'gender', 'editorial', 'formato', 'resume', 'creationDate', 'modificationDate']

    def to_representation(self, obj):
        book = Book.objects.get(ISBN=obj.ISBN)
        comments = list(Comment.objects.filter(book=obj.ISBN))
        print(comments)
        return {
            "ISBN": book.ISBN,
            "title": book.title,
            "volume": book.volume,
            "gender": book.gender,
            "editorial": book.editorial,
            "format": book.formato,
            "resume": book.resume,
            "url": book.url,
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
