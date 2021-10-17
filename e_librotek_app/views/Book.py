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

        filters = []
        try:
            filters = list(request.data["filters"])
        except:
            return response(400, messages=["There is no key 'filters' in the request body -> { ... 'filters' : [ ... ] ... }"])

        if len(filters) == 0:
            return response(400, messages=["The filters field is empty -> 'filters' : []"])

        query = {}
        limit = 1024
        try:
            limit = request.data["limit"]
        except:
            pass
        try:
            for filter in filters:
                if str(filter["option"]).lower() == "title":
                    query["title__icontains"] = filter["value"]
                if "token_type" in validData.keys():
                    if str(filter["option"]).lower() == "isbn":
                        query["ISBN"] = filter["value"]
                    elif str(filter["option"]).lower() == "gender":
                        query["gender"] = filter["value"]
                    elif str(filter["option"]).lower() == "editorial":
                        query["editorial__icontains"] = filter["value"]
        except Exception as e:
            return response(400, messages=["There is an error with the request body.", *e.args])
        try:
            books = self.queryset.filter(**query)
            start = 0
            end = len(books)
            try:
                start = request.data["offset"]["start"]
                end = request.data["offset"]["end"]
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
            except:
                pass

            res = []
            for i in range(start, end):
                if i <= limit:
                    serialized = self.serializer_class.to_representation(
                        self.serializer_class, obj=books[i])
                    res.append(serialized.copy())
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
        try:
            if "book" not in request.data.keys():
                return response(400, messages=["The key 'book' wasn't found in the request body (REQUIRED) -> { ... 'book' : {...} ... }"])
            messages = []
            if "ISBN" not in request.data["book"].keys():
                messages.append(
                    "The key 'ISBN' wasn't found in the 'book' object (REQUIRED) -> { ... 'book': { 'ISBN':'XXX' } ...}")
            elif len(request.data["book"]["ISBN"]) != 10 and len(request.data["book"]["ISBN"]) != 13:
                messages.append(
                    "The length of the value 'ISBN' must be 10 or 13 characters")
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
            self.queryset.filter(ISBN=request.data["ISBN"]).update(modificationDate=datetime.now(),
                                                                   ** request.data["book"])
            return response(200)
        except Exception as e:
            return response(500, messages=["There is an internal error", *e.args])
