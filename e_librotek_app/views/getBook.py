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


class GetBookView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
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
                # if "token_type" in validData.keys():
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
