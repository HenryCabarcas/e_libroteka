from django.conf import settings
from django.db.models.query import QuerySet
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from e_librotek_app.models import Book
from e_librotek_app.serializers import BookSerializer


class GetBook(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
            
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        return Response(self.serializer_class.to_representation(self.serializer_class, obj=self.queryset.get(ISBN=request.data["ISBN"])), status.HTTP_200_OK)
        return super().get(request, *args, **kwargs)
