from django.conf import settings
from django.db.models.query import QuerySet
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from e_librotek_app.models import Comment, book
from e_librotek_app.serializers import CommentSerializer


class GetComment(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
            
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        comments = self.queryset.filter(book=request.data["ISBN"])
        res = [self.serializer_class.to_representation(
            self.serializer_class, obj=comment) for comment in comments]
        return Response(res, status.HTTP_200_OK)