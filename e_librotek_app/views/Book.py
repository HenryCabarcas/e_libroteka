from django.conf import settings
from django.db.models.query import QuerySet
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from e_librotek_app.models import Book
from e_librotek_app.serializers import BookSerializer


class BookView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        valid_data = {}
        try:
            token = request.META.get('HTTP_AUTHORIZATION')[7:]
            tokenBackend = TokenBackend(
                algorithm=settings.SIMPLE_JWT['ALGORITHM'])
            valid_data = tokenBackend.decode(token, verify=False)
        except:
            pass
        filters = list(request.data["filters"])
        query = {}
        limit = 256
        try:
            limit = request.data["limit"]
        except:
            pass
        for filter in filters:
            if str(filter["option"]).lower() == "title":
                query["title__icontains"] = filter["value"]
            if "token_type" in valid_data.keys():
                if str(filter["option"]).lower() == "isbn":
                    query["ISBN"] = filter["value"]
                elif str(filter["option"]).lower() == "gender":
                    query["gender"] = filter["value"]
                elif str(filter["option"]).lower() == "editorial":
                    query["editorial__icontains"] = filter["value"]
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

        res = {
            "state": "success",
            "result": []
        }
        for i in range(start, end):
            if i <= limit:
                serialized = self.serializer_class.to_representation(
                    self.serializer_class, obj=books[i])
                res["result"].append(serialized.copy())
        return Response(res, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        res = {
            "status": "Success",
            "message": "The Book was successfully registered!",
            "code": 201
        }
        try:
            serializer = BookSerializer(data=request.data["book"])
            serializer.is_valid(raise_exception=True)
            serializer.save()
            '''
            tokenData = {
                "username": request.data['username'],
                "password": request.data['password']
            }
            tokenSerializer = TokenObtainPairSerializer(data=tokenData)
            tokenSerializer.is_valid(raise_exception=True)
            '''
        except Exception as e:
            res = {
                "status": "Error",
                "message": "There is an error with the request",
                "code": 500,
                "error": " ".join(str(e.args))
            }

        return Response(res, status=status.HTTP_201_CREATED)