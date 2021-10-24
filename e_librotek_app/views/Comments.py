from datetime import datetime

from django.conf import settings
from django.db.models import query
from django.db.models.query import QuerySet
from e_librotek_app.models import Comment, book
from e_librotek_app.responses_template import *
from e_librotek_app.serializers import CommentSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend

commentColumns = ['id', 'book', 'score', 'comment', 'user',
                  'creationDate', 'modificationDate']


class CommentView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        commentId = self.request.GET.get('id')
        bookISBN = self.request.GET.get('isbn')
        if bookISBN == None and commentId == None:
            return response(400, messages=["There must be the values 'book' or 'id' in the params."])
        query = {}
        try:
            if commentId != None:
                query["id"] = commentId
            if bookISBN != None:
                query["book"] = bookISBN
        except Exception as e:
            return response(400, messages=["There is an error with the request body.", *e.args])
        try:
            comments = self.queryset.filter(**query)
            if len(comments) == 0:
                ms = [
                    f"The comment id: {commentId} cannot be found in the database."]if commentId != None else []
                if bookISBN != None:
                    ms.append(
                        f"The book ISBN: {bookISBN} cannot be found in the database.")

                return response(400, messages=ms)

            res = [self.serializer_class.to_representation(
                self.serializer_class, obj=comment) for comment in comments]
            return response(200, result=res)
        except Exception as e:
            return response(500, messages=["There is an internal error", *e.args])

    def post(self, request, *args, **kwargs):
        try:
            token = request.META.get('HTTP_AUTHORIZATION')[7:]
            tokenBackend = TokenBackend(
                algorithm=settings.SIMPLE_JWT['ALGORITHM'])
            tokenBackend.decode(token, verify=False)
        except Exception as e:
            return response(400, messages=["There is no Auth token, it's REQUIRED  for this operation.", *e.args])
        if "comment" not in request.data.keys():
            return response(400, messages=["The key 'comment' it's REQUIRED."])
        serializer = CommentSerializer(data=request.data["comment"])
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return response(400, messages=["There is an error with the request", *e.args])
        try:
            serializer.save()
            return response(201, messages=["The Comment was successfully registered!"])
        except Exception as e:
            return response(500, messages=["There is an internal error", *e.args])

    def put(self, request, *args, **kwargs):
        try:
            token = request.META.get('HTTP_AUTHORIZATION')[7:]
            tokenBackend = TokenBackend(
                algorithm=settings.SIMPLE_JWT['ALGORITHM'])
            tokenBackend.decode(token, verify=False)
        except Exception as e:
            return response(400, messages=["There is no Auth token, it's REQUIRED  for this operation.", *e.args])
        try:
            if "id" not in request.data.keys():
                return response(400, messages=["There is no 'id' key in the request body, this value it's REQUIRED."])
            if "comment" not in request.data.keys():
                return response(400, messages=["There is no 'comment' key in the request body, this value it's REQUIRED."])
            if len(request.data["comment"].keys()) == 0:
                return response(400, messages=["The 'comment' object is empty."])
            for item in request.data["comment"].keys():
                if item not in commentColumns:
                    return response(400, messages=[f"The key: '{item}' isn't in the Comment model."])
        except Exception as e:
            return response(400, messages=["There is an error with the request body.", *e.args])
        try:
            result = self.queryset.filter(id=request.data["id"])
            if len(result) == 0:
                return response(400, messages=[f"The comment id: {request.data['id']} doesn't exist in the database."])
            result.update(modificationDate=datetime.now(),
                          **request.data["comment"])
            return response(200)
        except Exception as e:
            return response(500, messages=["There is an internal error", *e.args])
