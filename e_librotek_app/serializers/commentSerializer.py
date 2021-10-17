from e_librotek_app.models import Comment, Book
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'book', 'score', 'comment', 'user',
                  'creationDate', 'modificationDate']

    def to_representation(self, obj):
        print(obj)
        comment = Comment.objects.get(id=obj.id)
        return {
            "id": comment.id,
            "ISBN": comment.book.ISBN,
            "user": comment.user.username,
            "score": comment.score,
            "comment": comment.comment,
            "creationDate": comment.creationDate,
            "modificationDate": comment.modificationDate
        }
