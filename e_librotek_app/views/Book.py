from datetime import datetime

from django.conf import settings
from e_librotek_app.models import Book
from e_librotek_app.responses_template import *
from e_librotek_app.serializers import BookSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend

bookColumns = ['ISBN', 'title', 'volume',
               'gender', 'editorial', 'formato', 'resume', 'creationDate', 'modificationDate']


class BookView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        validData = {}
        try:
            token = request.META.get('HTTP_AUTHORIZATION')[7:]
            tokenBackend = TokenBackend(
                algorithm=settings.SIMPLE_JWT['ALGORITHM'])
            validData = tokenBackend.decode(token, verify=False)
        except:
            pass
        query = {}
        limit = 1024
        if self.request.GET.get('limit') != None:
            limit = self.request.GET.get('limit')
        if self.request.GET.get('title') != None:
            query["title__icontains"] = self.request.GET.get('title')
        if "token_type" in validData.keys():
            if self.request.GET.get('isbn') != None:
                query["ISBN"] = self.request.GET.get('isbn')
            if self.request.GET.get('gender') != None:
                query["gender__icontains"] = self.request.GET.get('gender')
            if self.request.GET.get('editorial') != None:
                query["editorial__icontains"] = self.request.GET.get(
                    'editorial')
        if len(query.keys()) == 0:
            return response(400, messages=["There is an error with the request params."])
        try:
            books = self.queryset.filter(**query)
            if len(books) == 0:
                return response(400, messages=["Cannot find that book."])
            res = []
            start = 0
            end = len(books)
            if self.request.GET.get('start') != None or self.request.GET.get('end') != None:
                if self.request.GET.get('start') != None:
                    start = self.request.GET.get('start')
                if self.request.GET.get('end') != None:
                    end = self.request.GET.get('end')
                if start >= len(books):
                    start = 0
                if end > len(books):
                    end = len(books)
                elif end <= 0:
                    end = len(books)+end
                elif end <= start:
                    end = len(books)
                else:
                    end += 1

            for i in range(start, end):
                if i <= limit:
                    serialized = self.serializer_class.to_representation(
                        self.serializer_class, obj=books[i])
                    res.append(serialized.copy())
            return response(200, result=res)
        except Exception as e:
            return response(500, messages=["There is an internal error", *e.args])

    def post(self, request, *args, **kwargs):
        # try:
        #     token = request.META.get('HTTP_AUTHORIZATION')[7:]
        #     tokenBackend = TokenBackend(
        #         algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        #     tokenBackend.decode(token, verify=False)
        # except Exception as e:
        #     return response(400, messages=["There is no Auth token, it's REQUIRED  for this operation.", *e.args])
        try:
            if "book" not in request.data.keys():
                return response(400, messages=["The key 'book' wasn't found in the request body (REQUIRED) -> { ... 'book' : {...} ... }"])
            messages = []
            if "ISBN" not in request.data["book"].keys():
                messages.append(
                    "The key 'ISBN' wasn't found in the 'book' object (REQUIRED) -> { ... 'book': { 'ISBN':'XXX' } ...}")
            elif len(request.data["book"]["ISBN"]) < 6 or len(request.data["book"]["ISBN"]) > 20:
                messages.append(
                    "The length of the value 'ISBN' must be between 6 and 20 characters")
            if "title" not in request.data["book"].keys():
                messages.append(
                    "The key 'title' wasn't found in the 'book' object (REQUIRED) -> { ... 'book': { 'title':'XXX' } ...}")
            elif len(request.data["book"]["title"]) <= 1:
                messages.append(
                    "The title length must be major than 1 character")

            if len(messages) > 0:
                return response(400, messages=messages)
        except Exception as e:
            return response(400, messages=["There is an error with the request body.", *e.args])
        serializer = BookSerializer(data=request.data["book"])
        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return response(400, messages=["There are problems with the request content.", *e.args])
        try:
            serializer.save()
            return response(201)
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
            if "ISBN" not in request.data.keys():
                return response(400, messages=["There is no 'ISBN' key in the request body, this value it's REQUIRED."])
            if "book" not in request.data.keys():
                return response(400, messages=["There is no 'book' key in the request body, this value it's REQUIRED."])
            if len(request.data["book"].keys()) == 0:
                return response(400, messages=["The 'book' object is empty."])
            for item in request.data["book"].keys():
                if item not in bookColumns:
                    return response(400, messages=[f"The key: '{item}' isn't in the Book model."])
        except Exception as e:
            return response(400, messages=["There is an error with the request body.", *e.args])
        try:
            result = self.queryset.filter(ISBN=request.data["ISBN"])
            if len(result) == 0:
                return response(400, messages=[f"The ISBN: {request.data['ISBN']} doesn't exist in the database."])
            result.update(
                modificationDate=datetime.now(), ** request.data["book"])
            return response(200)
        except Exception as e:
            return response(500, messages=["There is an internal error", *e.args])
